<template>
  <el-row>
    <el-tabs tab-position="left" style="height: 100%" @tab-click="tabs_switch">
      <el-tab-pane label="应用部署">
        <CommonDep ref="CommonDep"></CommonDep>
      </el-tab-pane>
      <el-tab-pane label="软件部署">
        <CommonDep ref="CommonDep"></CommonDep>
      </el-tab-pane>
      <el-tab-pane label="Kubernetes">
        <KubernetesDeploy ref="KubernetesDeploy"></KubernetesDeploy>
      </el-tab-pane>
    </el-tabs>
  </el-row>
</template>

<script>
import KubernetesDeploy from './kubernetes_deploy'
import CommonDep from './common_dep'
export default {
  name: 'soft_m',
  components: {
    KubernetesDeploy: KubernetesDeploy,
    CommonDep: CommonDep
  }
}
</script>

<style scoped>

</style>
