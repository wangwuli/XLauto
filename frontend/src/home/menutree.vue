<template>
  <div class="navMenu">

    <template v-for="navMenu in navMenus">
        <!-- 最后一级菜单 -->
      <el-menu-item v-if="!navMenu.childs"
                    :key="navMenu.id" :data="navMenu" :index="navMenu.name" @click="handleOpen2(navMenu)"
      >
        <i :class="navMenu.icon"></i>
        <span slot="title">{{navMenu.title}}</span>
      </el-menu-item>

      <!-- 此菜单下还有子菜单 -->
      <el-submenu v-if="navMenu.childs"
                  :key="navMenu.id" :data="navMenu" :index="navMenu.name">
        <template slot="title">
          <i :class="navMenu.icon"></i>
          <span> {{navMenu.title}}</span>
        </template>
        <!-- 递归 -->
        <NavMenu :navMenus="navMenu.childs"></NavMenu>
      </el-submenu>
    </template>

  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'NavMenu',
  props: ['navMenus'],
  data () { return {} },
  methods: {
    ...mapActions({
      handleOpen2: 'editableTabs'
    })
  }
}
</script>

<style>
  /* 水平样式 */
 .el-menu--horizontal>div>.el-submenu {
    float: left;
}
/* 一级菜单的样式 */
.el-menu--horizontal>div>.el-menu-item {
    float: left;
    height: 40px;
    line-height: 40px;
    margin: 0;
    border-bottom: 2px solid transparent;
    color: #909399;
}
/* 解决下图1 下拉三角图标 */
.el-menu--horizontal>div>.el-submenu .el-submenu__icon-arrow {
    position: static;
    vertical-align: middle;
    margin-left: 8px;
    margin-top: -3px;
}
/* 解决下图2 无下拉菜单时 不对齐问题 */
.el-menu--horizontal>div>.el-submenu .el-submenu__title {
    height: 40px;
    line-height: 40px;
    border-bottom: 2px solid transparent;
    color: #909399;
}

</style>

<!--thanks https://blog.csdn.net/qq_31126175/article/details/81875468-->
