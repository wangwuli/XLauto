<template>
  <el-row>
    <el-tabs tab-position="left" style="height: 100%" @tab-click="tabs_switch">
      <el-tab-pane label="安装绑定">
        <SoftInstallS ref="SoftInstallS"></SoftInstallS>
      </el-tab-pane>
      <el-tab-pane label="软件上传">
        <SoftPackageS ref="SoftPackageS"></SoftPackageS>
      </el-tab-pane>
      <el-tab-pane label="配置管理">
        <SoftConfiguration ref="SoftConfiguration"></SoftConfiguration>
      </el-tab-pane>
      <el-tab-pane label="待开发">
      </el-tab-pane>
    </el-tabs>
  </el-row>
</template>

<script>
import SoftInstallS from './soft_install_s'
import SoftConfiguration from './soft_configuration'
import SoftPackageS from './soft_package_s'
export default {
  name: 'soft_m',
  components: {
    SoftInstallS: SoftInstallS,
    SoftConfiguration: SoftConfiguration,
    SoftPackageS: SoftPackageS
  }
}
</script>

<style scoped>

</style>
