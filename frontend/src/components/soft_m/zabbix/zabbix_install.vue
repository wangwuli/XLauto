<template>
  <el-row>
    <el-button type="primary" size="mini" @click="hosts_add_target">主机加入<i
      class="el-icon-circle-plus-outline el-icon--right"></i></el-button>
    <el-button type="primary" size="mini">查询</el-button>
    <el-button type="primary" size="mini">同步</el-button>
    <el-button type="primary" size="mini">安装</el-button>
    <el-select
      size="mini"
      v-model="zabbix_hots_groups"
      filterable
      multiple
      collapse-tags
      style="margin-left: 20px;width: 350px"
      placeholder="全选Zabbix组">
      <el-option
        v-for="item in zabbix_hots_groups_list"
        :key="item.groupid"
        :label="item.name"
        :value="item.groupid">
      </el-option>
    </el-select>
    <el-select
      popper-append-to-body="false"
      @change="all_templateids_change"
      size="mini"
      v-model="zabbix_templateids"
      multiple
      filterable
      collapse-tags
      style="margin-left: 20px; width: 350px"
      placeholder="全选Zabbix模板">
      <el-option
        filterable
        v-for="item in zabbix_templateids_list"
        :key="item.templateid"
        :label="item.name"
        :value="item.templateid">
      </el-option>
    </el-select>
    <el-table
      :row-style="{height:'20px'}"
      :cell-style="{padding:'0px'}"
      style="font-size: 10px;width: 100%"
      size="mini"
      :data="hosts_table_data"
      :row-class-name="tableRowClassName">
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
      <el-table-column
        label="Zabbix主机组"
        show-overflow-tooltip>
        <template slot-scope='hots_groups'>
          <el-select
            size="mini"
            v-model="hots_groups.row.zabbix_hots_groups"
            multiple
            collapse-tags
            placeholder="请选择">
            <el-option
              v-for="item in hots_groups.row.zabbix_hots_groups_list"
              :key="item.groupid"
              :label="item.name"
              :value="item.groupid">
            </el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column
        label="Zabbix主机名"
        show-overflow-tooltip>
        <template slot-scope='host_name'>
          <el-input size="mini" v-model="host_name.row.zabbix_host_name" placeholder="请输入内容"></el-input>
        </template>
      </el-table-column>
      <el-table-column
        label="Zabbix模板"
        width="350px">
        <template slot-scope='zabbix_template'>
          <el-select
            style="width: 300px"
            filterable
            size="mini"
            v-model="zabbix_template.row.zabbix_templateids"
            multiple
            collapse-tags
            placeholder="请选择">
            <el-option
              v-for="item in zabbix_templateids_list"
              :key="item.templateid"
              :label="item.name"
              :value="item.templateid">
            </el-option>
          </el-select>
        </template>
      </el-table-column>
  </el-table>
  </el-row>
</template>

<script>
import { mapState } from 'vuex'
import * as Request from '@/general/request.js'

export default {
  name: 'zabbix',
  created () {
    this.zabbix_templates_query()
  },
  data () {
    return {
      zabbix_hots_groups_list: [],
      zabbix_hots_groups: [],
      zabbix_templateids_list: [],
      zabbix_templateids: [],
      // hosts_table_data: []
      hosts_table_data: [{
        host_ip: '2016-05-01',
        host_name: '王小虎',
        install_info: '上海市普陀区金沙江路 1518 弄',
        execute_result: 1,
        zabbix_hots_groups_list: [{
          groupid: '2',
          name: 'Linux servers',
          internal: '0'
        }],
        zabbix_hots_groups: [],
        zabbix_templateids_list: [{
          templateid: '2',
          name: 'Linux template',
          internal: '0'
        }],
        zabbix_templateids: [],
        zabbix_host_name: 'ahahah'
      }, {
        host_ip: '2016-05-03',
        host_name: '王小虎',
        install_info: '上海市普陀区金沙江路 1518 弄',
        execute_result: 0,
        zabbix_hots_groups_list: [],
        zabbix_hots_groups: []
      }]
    }
  },
  computed: {
    ...mapState({
      table_click_value: 'hosts_table_click_values',
      background_socket: 'background_socket'
    })
  },
  methods: {
    all_templateids_change () {
      this.hosts_table_data.map((item) => {
        item.zabbix_templateids = this.zabbix_templateids
      })
    },
    hosts_add_target () {
      if (this.table_click_value) {
        this.hosts_table_data = JSON.parse(JSON.stringify(this.table_click_value))
      } else {
        this.$message.warning('标靶中无选中服务器')
      }
    },
    async zabbix_templates_query () {
      const response = await Request.GET('/deploy/zabbix/templates')
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          // this.$message.success(data.msg)
          this.zabbix_templateids_list = data.data
        } else {
          this.$message.error(data.msg)
        }
      }
    }
  }
}
</script>

<style scoped>
  /deep/ .el-select__tags-text  {
    display: inline-block;
    max-width: 80px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .el-select /deep/ .el-tag__close.el-icon-close {
    top: -5px;
  }
</style>
