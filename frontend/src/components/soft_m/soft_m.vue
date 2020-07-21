<template>
  <el-row>
    <el-tabs tab-position="left" style="height: 100%" @tab-click="tabs_switch">
      <el-tab-pane label="Kubernetes">
        <KubernetesDeploy ref="KubernetesDeploy"></KubernetesDeploy>
      </el-tab-pane>
      <el-tab-pane label="待开发">角色管理</el-tab-pane>
    </el-tabs>
  </el-row>
</template>

<script>
import KubernetesDeploy from './kubernetes_deploy'
export default {
  name: 'soft_m',
  components: {
    KubernetesDeploy: KubernetesDeploy
  }
}
</script>

<style scoped>

</style>
