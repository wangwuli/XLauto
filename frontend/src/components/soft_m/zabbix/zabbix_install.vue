<template>
  <el-row>
    <el-button type="primary" size="mini" @click="hosts_add_target">主机加入<i class="el-icon-circle-plus-outline el-icon--right"></i></el-button>
    <el-button type="primary" size="mini">查询</el-button>
    <el-button type="primary" size="mini">同步</el-button>
    <el-button type="primary" size="mini">安装</el-button>
    <el-table
    :row-style="{height:'20px'}"
    :cell-style="{padding:'0px'}"
    style="font-size: 10px;width: 100%"
    size="mini"
    :data="hosts_table_data"
    :row-class-name="tableRowClassName"
    @selection-change="handleSelectionChange">
    <el-table-column
      type="selection"
      width="55">
    </el-table-column>
    <el-table-column
      prop="host_ip"
      label="IP"
      width="180">
    </el-table-column>
    <el-table-column
      prop="host_name"
      label="主机名"
      width="180">
    </el-table-column>
    <el-table-column
      prop="install_info"
      label="安装信息"
    show-overflow-tooltip>
    </el-table-column>
      <el-table-column
        label="结果"
        show-overflow-tooltip>
        <template slot-scope='if_execute_result_icon'>
          <i class="el-icon-error" v-if="if_execute_result_icon.row.execute_result == -1"
             style="font-size: 15px; color: #F56C6C"/>
          <i class="el-icon-success" v-if="if_execute_result_icon.row.execute_result == 1"
             style="font-size: 15px; color: #67C23A"/>
          <i class="el-icon-warning" v-if="if_execute_result_icon.row.execute_result == 2"
             style="font-size: 15px; color: #E6A23C"/>
          <i class="el-icon-question" v-if="if_execute_result_icon.row.execute_result == 0"
             style="font-size: 15px; color: #909399"/>
        </template>
      </el-table-column>
  </el-table>
  </el-row>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'zabbix',
  data () {
    return {
      hosts_table_data: []
      // hosts_table_data: [{
      //   host_ip: '2016-05-01',
      //   host_name: '王小虎',
      //   install_info: '上海市普陀区金沙江路 1518 弄',
      //   execute_result: 1
      // }, {
      //   host_ip: '2016-05-03',
      //   host_name: '王小虎',
      //   install_info: '上海市普陀区金沙江路 1518 弄',
      //   execute_result: 0
      // }]
    }
  },
  computed: {
    ...mapState({
      table_click_value: 'hosts_table_click_values',
      background_socket: 'background_socket'
    })
  },
  methods: {
    hosts_add_target () {
      if (this.table_click_value) {
        this.hosts_table_data = JSON.parse(JSON.stringify(this.table_click_value))
      } else {
        this.$message.warning('标靶中无选中服务器')
      }
    }
  }
}
</script>

<style>
</style>
