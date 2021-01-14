<template>
  <el-row>
    <el-row>
      <el-col :span="24">
        <el-button type="primary" size="mini" @click="adddialog = true">本地新增</el-button>
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
          prop="software_conf_path"
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
        :data="tableData"
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
  </el-row>
</template>

<script>
import * as Request from '@/general/request.js'
export default {
  created () {
    this.software_package_query()
  },
  data () {
    return {
      soft_table_data: [],
      currentRow: null
    }
  },
  methods: {
    handleCurrentChange (val) {
      this.currentRow = val
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
