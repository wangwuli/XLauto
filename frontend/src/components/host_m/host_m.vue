<template>
  <el-row>
    <el-tabs :tab-position="tabPosition" style="height: 100%" @tab-click="tabs_switch">
      <el-tab-pane label="主机信息">
        <HostInfo ref="hotsInfo"></HostInfo>
      </el-tab-pane>
      <el-tab-pane label="命令推送">
        <HostCmd ref="hotsCmd"></HostCmd>
      </el-tab-pane>
      <el-tab-pane label="待开发">角色管理</el-tab-pane>
    </el-tabs>
  </el-row>
</template>
<script>
import HostInfo from './host_info'
import HostCmd from './host_cmd'

export default {
  name: 'host_m',
  components: {
    HostInfo: HostInfo,
    HostCmd: HostCmd
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
    tabs_switch (tab) {
      if (tab.label === '主机信息') {
        this.$refs.hotsInfo.start_fulsh()
      } else {
        this.$refs.hotsInfo.stop_flush()
      }
      if (tab.label === '命令推送') {
        this.$refs.hotsCmd.created_tabs_switch()
      }
    }
  },
  computed: {
  }
}
</script>
<style scoped>
</style>
