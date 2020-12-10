<template>
  <el-row>
    <el-button type="primary" size="mini" @click="hosts_add_target">主机加入<i
      class="el-icon-circle-plus-outline el-icon--right"></i></el-button>
    <el-button type="primary" size="mini" @click="zabbix_agents_install_info_query">查询</el-button>
    <el-tooltip class="item" effect="dark" content="使用：{IP.project_code}为名字，去Zabbix内与hostname进行匹配" placement="top-start">
      <el-button type="primary" size="mini" @click="zabbix_agents_install_info_sync">同步</el-button>
    </el-tooltip>
    <el-button type="primary" size="mini" @click="zabbix_agents_install_exec">安装</el-button>
    <el-select
      @change="all_host_groups_change"
      size="mini"
      v-model="zabbix_hots_groups"
      filterable
      multiple
      collapse-tags
      style="margin-left: 20px;width: 280px"
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
      style="margin-left: 20px; width: 280px"
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
      ref="hosts_table_data_ref"
      :row-style="{height:'20px'}"
      :cell-style="{padding:'0px'}"
      style="font-size: 10px;width: 100%"
      size="mini"
      :data="hosts_table_data">
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
        prop="project_code"
        label="项目编号"
        show-overflow-tooltip>
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
        prop="operate_time"
        label="同步时间"
        show-overflow-tooltip>
      </el-table-column>
      <el-table-column
        label="结果"
        width="50px">
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
        label="Zabbix主机名"
        width="165px"
        >
        <template slot-scope='host_name'>
          <el-input size="mini" v-model="host_name.row.zabbix_host_name" placeholder="无"></el-input>
        </template>
      </el-table-column>
      <el-table-column
        width="250px"
        label="Zabbix主机组"
        >
        <template slot-scope='hots_groups'>
          <el-select
            filterable
            style="width: 240px"
            size="mini"
            v-model="hots_groups.row.zabbix_hots_groups"
            multiple
            collapse-tags
            placeholder="请选择">
            <el-option
              v-for="item in zabbix_hots_groups_list"
              :key="item.groupid"
              :label="item.name"
              :value="item.groupid">
            </el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column
        label="Zabbix模板"
        width="250px">
        <template slot-scope='zabbix_template'>
          <el-select
            style="width: 240px"
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
    this.zabbix_host_groups_query()
  },
  data () {
    return {
      zabbix_hots_groups_list: [],
      zabbix_hots_groups: [],
      zabbix_templateids_list: [],
      zabbix_templateids: [],
      // hosts_table_data: []
      hosts_table_data: []
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
    all_host_groups_change () {
      this.hosts_table_data.map((item) => {
        item.zabbix_hots_groups = this.zabbix_hots_groups
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
    },
    async zabbix_host_groups_query () {
      const response = await Request.GET('/deploy/zabbix/host_groups')
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          // this.$message.success(data.msg)
          this.zabbix_hots_groups_list = data.data
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    hosts_table_data_updata (data) {
      var returnData = []
      data.map((item) => {
        var ifOkk = true
        for (let ai = 0; ai < this.hosts_table_data.length; ai++) {
          if (item.host_id === this.hosts_table_data[ai].host_id) {
            item.zabbix_hots_groups = item.zabbix_groupids.split(',')
            item.zabbix_templateids = item.zabbix_templateids.split(',')
            returnData.push(item)
            ifOkk = false
            continue
          }
        }
        if (ifOkk) {
          returnData.push(item)
        }
      })
      if (returnData.length) {
        this.hosts_table_data = returnData
      }
    },
    async zabbix_agents_install_info_query () {
      if (!this.$refs.hosts_table_data_ref.selection.length) {
        this.$message.warning('请勾选需要查询的服务器')
        return
      }
      var hotsIds = []
      this.$refs.hosts_table_data_ref.selection.map((item) => {
        hotsIds.push(item.host_id)
      })
      this.$message.info('正在查询请稍后...')
      const response = await Request.GET('/deploy/zabbix/agents_install', { host_ids: hotsIds.join() })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.$message.success('查询成功')
          // this.$message.success(data.msg)
          // 替换查询到的数据，未查询数到的数据不发生改变
          this.hosts_table_data_updata(data.data)
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    async zabbix_agents_install_info_sync () {
      if (!this.$refs.hosts_table_data_ref.selection.length) {
        this.$message.warning('请勾选需要同步的服务器')
        return
      }
      var hotsIds = []
      this.$refs.hosts_table_data_ref.selection.map((item) => {
        hotsIds.push(item.host_id)
      })
      this.$message.info('正在同步请稍后')
      const response = await Request.POST('/deploy/zabbix/agents_install', { host_ids: hotsIds })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.$message.success('同步成功')
          this.hosts_table_data_updata(data.data)
          // this.zabbix_agents_install_info_query()
        } else {
          this.$message.error('同步失败:' + data.msg)
        }
      }
    },
    async zabbix_agents_install_exec () {
      if (!this.$refs.hosts_table_data_ref.selection.length) {
        this.$message.warning('请勾选需要查询的服务器')
        return
      }
      this.$message.info('正在安装请稍后...')
      const response = await Request.PUT('/deploy/zabbix/agents_install', { hosts_table_data: this.hosts_table_data })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.$message.success('安装成功')
          // 替换查询到的数据，未查询数到的数据不发生改变
          // this.hosts_table_data_updata(data.data)
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
