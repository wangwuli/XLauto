<template>
  <el-container style="padding-left:0">
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
      <NavMenu :navMenus="menuData"  :style="{width: clientW + 'px'}"></NavMenu> <!-- 我是菜单栏组件 -->
<!--      "width:50%;overflow-x:auto;"-->
    </el-menu>
  </el-header>
  <el-main style="padding-right: 8px;padding-left: 8px;">
    <mainTabs /> <!-- 我是tabs组件 -->
  </el-main>
  <el-aside>
    <upperbutton /> <!-- 我是悬浮按钮组件 -->
  </el-aside>
  </el-container>
</template>

<script>
import NavMenu from '@/home/menutree'
import * as Request from './general/request.js'
import mainTabs from '@/home/tabs'
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
      clientW: document.documentElement.clientWidth
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
  html,body,#app,.el-container {
    /*设置内部填充为0，几个布局元素之间没有间距*/
    padding: 0px;
    /*外部间距也是如此设置*/
    margin: 0px;
    /*统一设置高度为100%*/
  }
/*
下面这样是重新定义菜单宽度
*/
.el-menu--collapse .el-menu .el-submenu, .el-menu--popup {
screenHeighth: 1000px;
}
</style>
<!--thanks https://blog.csdn.net/qq_31126175/article/details/81875468-->
