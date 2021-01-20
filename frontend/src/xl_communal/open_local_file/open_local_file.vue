<template>
  <el-row>
    <el-input v-model="current_directory" size="mini" @keyup.enter.native="current_directory_r"></el-input>
    <el-table
      @row-dblclick="table_dblclick"
      highlight-current-row
      :row-style="{height:'20px'}"
      :cell-style="{padding:'0px'}"
      size="mini"
      :data="file_table_data"
      style="width: 80%">
      <el-table-column
        type="index"
        width="50">
      </el-table-column>
      <el-table-column
        show-overflow-tooltip
        prop="file_name"
        label="名称">
      </el-table-column>
      <el-table-column
        show-overflow-tooltip
        prop="file_type"
        label="属性">
      </el-table-column>
    </el-table>
    <el-dialog title="确认选择双击文件" :visible.sync="dialog_file" append-to-body>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialog_file = false">取 消</el-button>
        <el-button type="primary" @click="submit_select_r">确 定</el-button>
      </div>
    </el-dialog>
  </el-row>
</template>

<script>
import * as Request from '@/general/request.js'
export default {
  data () {
    return {
      file_data_all: '',
      file_table_data: [{
        file_name: '',
        file_type: '',
        file_path: ''
      }],
      current_directory: '/',
      dialog_file: false,
      submit_select: [],
      submit_select_swap: []
    }
  },
  name: 'open_local_file',
  props: {
    software_package_id: {
      type: Number,
      default: null
    }
  },
  mounted () {
    this.get_file_list(this.software_package_id)
  },
  watch: {
    submit_select (val) {
      this.$emit('submit_select_data', val)
    },
    software_package_id (val) {
      this.get_file_list(val)
    }
  },
  methods: {
    close_dialog_file () {
      this.dialog_file = false
    },
    current_directory_r () {
      if (this.file_data_all.indexOf(this.current_directory) === -1) {
        this.$message.error('错误的路径')
      } else {
        this.current_dir()
      }
    },
    submit_select_r () {
      this.submit_select = JSON.parse(JSON.stringify(this.submit_select_swap))
    },
    table_dblclick (row) {
      if (row.file_name === '..') {
        var swapPath = this.current_directory.replace(this.current_directory_root, '')
        var swapPathList = swapPath.split('/')
        if (swapPathList.length === 1 || swapPathList.length === 2) {
          this.current_directory = this.current_directory_root
        } else {
          swapPathList = swapPathList.slice(0, -2)
          this.current_directory = this.current_directory_root + swapPathList.join('/') + '/'
        }
        this.current_dir()
      } else if (row.file_type === 'd') {
        this.current_directory = row.file_path
        this.current_dir()
      } else {
        this.submit_select_swap = row
        this.dialog_file = true
      }
    },
    async get_file_list (softwarePackageId) {
      const response = await Request.GET('/file/local_dir', { software_package_id: softwarePackageId })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.file_data_all = data.data.package_path_dir_list
          this.current_directory_root = data.data.package_path
          this.current_directory = data.data.package_path
          this.current_dir()
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    current_dir () {
      var FileTableData = [{
        file_name: '..',
        file_type: 'd',
        file_path: ''
      }]
      this.file_data_all.map((item) => {
        var swapFile = item.replace(this.current_directory, '').split('/')
        if (swapFile.length === 2 && swapFile[1] === '') {
          FileTableData.push({
            file_name: swapFile[0],
            file_type: 'd',
            file_path: item
          })
        } else if (swapFile.length === 1) {
          if (swapFile[0] === '') {
            FileTableData.push({
              file_name: '.',
              file_type: 'd',
              file_path: item
            })
          } else {
            FileTableData.push({
              file_name: swapFile[0],
              file_type: 'f',
              file_path: item
            })
          }
        }
      })
      this.file_table_data = FileTableData
    }
  }
}
</script>

<style scoped>

</style>
