<template>
  <el-row>
    <el-row>
      <el-col :span="24">
        <el-button type="primary" size="mini" @click="open_soft_dir">新增配置</el-button>
      </el-col>
    </el-row>
    <el-row>
    <el-col :span="7">
      <el-table
        @current-change="handleCurrentChange"
        highlight-current-row
        :row-style="{height:'20px'}"
        :cell-style="{padding:'0px'}"
        size="mini"
        :data="soft_table_data"
        style="width: 80%">
        <el-table-column
          type="index"
          width="50">
        </el-table-column>
        <el-table-column
          prop="software_name"
          label="软件">
        </el-table-column>
        <el-table-column
          prop="software_versions"
          label="版本">
        </el-table-column>
      </el-table>
    </el-col>
    <el-col :span="1">
      <el-divider direction="vertical"></el-divider>
    </el-col>
    <el-col :span="7">
      <el-table
        :row-style="{height:'20px'}"
        :cell-style="{padding:'0px'}"
        size="mini"
        :data="software_conf_data"
        style="width: 80%">
        <el-table-column
          fixed
          prop="software_name"
          label="软件">
        </el-table-column>
        <el-table-column
          prop="software_conf_path"
          label="配置文件">
        </el-table-column>
      </el-table>
    </el-col>
    <el-col :span="1">
      <el-divider direction="vertical"></el-divider>
    </el-col>
    <el-col :span="7">
      <el-tabs type="border-card">
        <el-tab-pane label="用户管理">用户管理</el-tab-pane>
        <el-tab-pane label="配置管理">配置管理</el-tab-pane>
        <el-tab-pane label="角色管理">角色管理</el-tab-pane>
        <el-tab-pane label="定时任务补偿">定时任务补偿</el-tab-pane>
      </el-tabs>
    </el-col>
  </el-row>

    <el-dialog :visible.sync="file_dialog">
      <OpenLocalFile :software_package_id="software_package_id" @submit_select_data="submit_select_data"></OpenLocalFile>
    </el-dialog>

  </el-row>
</template>

<script>
import * as Request from '@/general/request.js'
import { OpenLocalFile } from '@/xl_communal'
export default {
  components: {
    OpenLocalFile: OpenLocalFile
  },
  created () {
    this.software_package_query()
  },
  data () {
    return {
      soft_table_data: [],
      software_conf_data: [],
      currentRow: null,
      software_package_id: '',
      file_dialog: false
    }
  },
  methods: {
    submit_select_data (val) {
      debugger
    },
    open_soft_dir () {
      this.file_dialog = true
    },
    handleCurrentChange (val) {
      this.software_package_id = val.software_package_id
      this.software_conf_query(val.software_package_id)
    },
    async software_package_query () {
      const response = await Request.GET('/deploy/soft_package')
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.soft_table_data = data.data
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    async software_conf_query (softwarePackageId) {
      const response = await Request.GET('/deploy/software_conf', { software_package_id: softwarePackageId })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.software_conf_data = data.data
        } else {
          this.$message.error(data.msg)
        }
      }
    }
  }
}
</script>

<style scoped>
  /deep/ .el-table__fixed-right {
    height: 100% !important;
  }
  /deep/ .el-table__fixed {
    height: 100% !important;
  }
</style>
