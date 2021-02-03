<template>
  <el-row>
    <el-row>
      <el-col :span="24">
        <el-button type="success" size="mini" @click="open_soft_dir">新增配置</el-button>
        <el-button type="danger" size="mini" @click="del_software_conf_dialog = true">删除配置</el-button>
        <select-sys-code
          style="width: 15%; margin-left: 5px"
          code_type="software_conf_type"
          v-model="software_conf_type"
        ></select-sys-code>
        <el-button type="primary" size="mini" @click="software_conf_parameter_analysis">分析配置</el-button>
        <el-button style="margin-left: 5px" icon="el-icon-search" size="mini" @click="software_package_query">刷新</el-button>
      </el-col>
    </el-row>
    <el-row>
    <el-col :span="5">
      <el-table
        @row-click="handleCurrentChange"
        highlight-current-row
        :row-style="{height:'20px'}"
        :cell-style="{padding:'0px'}"
        size="mini"
        :data="soft_table_data"
        style="width: 95%">
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
    <el-col :span="0.8">
      <el-divider direction="vertical"></el-divider>
    </el-col>
    <el-col :span="6">
      <el-table
        ref="software_conf_data_ref"
        @row-click="conf_change"
        highlight-current-row
        :row-style="{height:'20px'}"
        :cell-style="{padding:'0px'}"
        size="mini"
        :data="software_conf_data"
        style="width: 98%">
        <el-table-column
          type="selection"
          width="55">
        </el-table-column>
        <el-table-column
          show-overflow-tooltip
          fixed
          prop="software_conf_name"
          label="配置文件">
        </el-table-column>
        <el-table-column
          show-overflow-tooltip
          prop="software_conf_path"
          label="配置路径">
        </el-table-column>
      </el-table>
    </el-col>
    <el-col :span="0.8">
      <el-divider direction="vertical"></el-divider>
    </el-col>
    <el-col :span="12">
      <el-tabs type="border-card">
        <el-tab-pane label="配置项">
          <el-button size="mini" type="primary" icon="el-icon-edit" circle></el-button>
          <el-button size="mini" type="success" icon="el-icon-check" circle></el-button>
          <el-button size="mini" type="danger" icon="el-icon-delete" circle></el-button>
          <el-table
            @row-click="conf_change"
            highlight-current-row
            :row-style="{height:'20px'}"
            :cell-style="{padding:'0px'}"
            size="mini"
            :data="software_conf_parameter_data"
            style="width: 98%">
            <el-table-column
              type="selection"
              width="55">
            </el-table-column>
            <el-table-column
              show-overflow-tooltip
              fixed
              prop="replacement_entry"
              label="参数">
            </el-table-column>
            <el-table-column
              show-overflow-tooltip
              prop="replacement_value"
              label="默认值">
            </el-table-column>
          </el-table>
        </el-tab-pane>
        <el-tab-pane label="配置管理">配置管理</el-tab-pane>
        <el-tab-pane label="角色管理">角色管理</el-tab-pane>
        <el-tab-pane label="定时任务补偿">定时任务补偿</el-tab-pane>
      </el-tabs>
    </el-col>
  </el-row>

    <el-dialog :visible.sync="file_dialog">
      <OpenLocalFile :software_package_id="software_package_id" @submit_select_data="submit_select_data" ref="open_local_file_ref"></OpenLocalFile>
    </el-dialog>

    <el-dialog title="确认清除勾选配置文件记录" :visible.sync="del_software_conf_dialog" width="500px" >
      <div slot="footer" class="dialog-footer">
        <el-button @click="del_software_conf_dialog = false" size="mini">取 消</el-button>
        <el-button type="primary" @click="del_software_conf" size="mini">确 定</el-button>
      </div>
    </el-dialog>
  </el-row>
</template>

<script>
import * as Request from '@/general/request.js'
import { OpenLocalFile, SelectSysCode } from '@/xl_communal'
export default {
  components: {
    OpenLocalFile: OpenLocalFile,
    SelectSysCode: SelectSysCode
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
      file_dialog: false,
      software_conf_parameter_data: [],
      del_software_conf_dialog: false,
      software_conf_type: ''
    }
  },
  methods: {
    submit_select_data (val) { // 传入子模块的方法,等待子模块调用
      val.software_package_id = this.software_package_id
      this.save_software_conf(val)
    },
    open_soft_dir () {
      this.file_dialog = true
    },
    handleCurrentChange (val) {
      this.software_package_id = val.software_package_id
      this.software_conf_query()
    },
    conf_change (val) {
      this.get_software_conf_parameter(val.software_conf_id)
    },
    async get_software_conf_parameter (val) {
      const response = await Request.GET('/deploy/software_conf_parameter', { software_conf_id: val })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.software_conf_parameter_data = data.data
          this.$message.success(data.msg)
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    async save_software_conf (val) {
      const response = await Request.POST('/deploy/software_conf', { software_conf_data: val })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.$refs.open_local_file_ref.close_dialog_file()
          this.software_conf_query()
          this.$message.success(data.msg)
        } else {
          this.$message.error(data.msg)
        }
      }
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
    async software_conf_query () {
      const response = await Request.GET('/deploy/software_conf', { software_package_id: this.software_package_id })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.software_conf_data = data.data
          this.$message.success(data.msg)
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    get_software_conf_ids () {
      var softwareConfids = []
      this.$refs.software_conf_data_ref.selection.map((item) => {
        softwareConfids.push(item.software_conf_id)
      })
      if (softwareConfids.length) {
        return softwareConfids
      } else {
        this.$message.error('请勾选一个配置文件')
      }
    },
    async del_software_conf () {
      var softwareConfids = this.get_software_conf_ids()
      const response = await Request.DELETE('/deploy/software_conf', { software_conf_ids: softwareConfids })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.$message.success(data.msg)
          this.del_software_conf_dialog = false
          this.software_conf_query()
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    async software_conf_parameter_analysis () {
      // var softwareConfids = this.get_software_conf_ids()
      var softwareConfinfo = this.$refs.software_conf_data_ref.selection
      const response = await Request.POST('/deploy/software_conf_parameter/analysis',
        {
          software_conf_info: softwareConfinfo,
          software_conf_type: this.software_conf_type
        })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          // this.software_conf_parameter_data = data.data
          this.$message.success(data.msg)
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
