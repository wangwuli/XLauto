<template>
  <el-row>
    <el-tabs :tab-position="tabPosition" style="height: 100%" @tab-click="tabs_switch">
      <el-tab-pane label="Zabbix">
        <Zabbix ref="zabbix_ref"></Zabbix>
      </el-tab-pane>
      <el-tab-pane label="待开发">待开发</el-tab-pane>
    </el-tabs>
  </el-row>
</template>
<script>
import Zabbix from './zabbix/zabbix'
// import HostCmd from './host_cmd'
// import HostCommon from './host_common'

export default {
  name: 'setting',
  components: {
    Zabbix: Zabbix
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
