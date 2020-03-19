<template>
  <el-container>
    <el-header style="padding-right: 0px;padding-left: 0px;">
    <el-menu
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      :default-active="activeIndex"
      router
      mode="horizontal"
      width="100%"
    >
      <NavMenu :navMenus="menuData" style="width:800px;overflow-x:auto;"></NavMenu>
    </el-menu>
  </el-header>
  <el-main style="padding-right: 0px;padding-left: 0px;">
    <mainTabs></mainTabs> <!-- 我是tabs组件 -->
  </el-main>
  <el-aside>
    <upperbutton />
  </el-aside>
  </el-container>
</template>

<script>
import NavMenu from '@/home/menutree'
import * as Request from './general/request.js'
import mainTabs from '@/home/tabs'
// import allDrawer from '@/home/alldrawer'
import upperbutton from '@/home/upperbutton'

export default {
  created () {
    this.homemenuQuery()
  },

  components: {
    NavMenu: NavMenu,
    mainTabs: mainTabs,
    upperbutton: upperbutton
  },
  data () {
    return {
      activeIndex: '主页',
      menuData: [],
      editableTabsValue: '2',
      editableTabs: [],
      tabIndex: 2
    }
  },
  methods: {
    async homemenuQuery () {
      const response = await Request.GET('/home/menu_query')
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.$message.success(data.msg)
          this.menuData = data.data
        } else {
          this.$message.error(data.msg)
        }
      }
    }
  }
}
</script>

<style>
  * {
    outline: none;
  }
</style>
<!--thanks https://blog.csdn.net/qq_31126175/article/details/81875468-->
