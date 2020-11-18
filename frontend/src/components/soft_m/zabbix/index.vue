<template>
  <el-row>
    <el-tabs :tab-position="tabPosition" style="height: 100%" @tab-click="tabs_switch">
      <el-tab-pane label="安装监控">
        <ZabbixInstall ref="zabbix_management_ref"></ZabbixInstall>
      </el-tab-pane>
      <el-tab-pane label="模板管理">待开发</el-tab-pane>
      <el-tab-pane label="绑定模板">待开发</el-tab-pane>
    </el-tabs>
  </el-row>
</template>
<script>
import ZabbixInstall from './zabbix_install'
// import HostCmd from './host_cmd'
// import HostCommon from './host_common'

export default {
  name: 'setting',
  components: {
    ZabbixInstall: ZabbixInstall
  //   HostCmd: HostCmd,
  //   HostCommon: HostCommon
  },
  data () {
    return {
      tabPosition: 'left'
    }
  },
  destroyed () {
  },
  mounted () {
  },
  methods: {
  },
  computed: {
  }
}
</script>
<style scoped>
</style>
