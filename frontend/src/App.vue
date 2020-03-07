import axios from 'axios'

<template>
  <el-container>
    <el-header>
      <el-menu
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
        :default-active="activeIndex"
        router
        mode="horizontal"
      >
        <NavMenu :navMenus="menuData" style="width:800px;overflow-x:auto;"></NavMenu>
      </el-menu>

    </el-header>

    <el-main>
      <el-tabs v-model="editableTabsValue" type="card" closable @tab-remove="removeTab">
        <el-tab-pane
          v-for="(item, index) in editableTabs"
          :key="item.name"
          :label="item.title"
          :name="item.name"
        >
          {{item.content}}
        </el-tab-pane>
      </el-tabs>
    </el-main>

  </el-container>

</template>

<script>
  import NavMenu from "./home/menutree";
  import * as Request from "./general/request.js";

  export default {
    created() {
      this.homemenuQuery()
    },

    components: {
      NavMenu: NavMenu
    },
    data() {
      return {
        menuData: [],
        editableTabsValue: '2',
        editableTabs: [{
          title: 'Tab 1',
          name: '1',
          content: 'Tab 1 content'
        }, {
          title: 'Tab 2',
          name: '2',
          content: 'Tab 2 content'
        }],
        tabIndex: 2
      }
    },
    methods: {
      addTab(targetName) {
        let newTabName = ++this.tabIndex + '';
        this.editableTabs.push({
          title: targetName,
          name: newTabName,
          content: 'New Tab content'
        });
        this.editableTabsValue = newTabName;
      },
      removeTab(targetName) {
        let tabs = this.editableTabs;
        let activeName = this.editableTabsValue;
        if (activeName === targetName) {
          tabs.forEach((tab, index) => {
            if (tab.name === targetName) {
              let nextTab = tabs[index + 1] || tabs[index - 1];
              if (nextTab) {
                activeName = nextTab.name;
              }
            }
          });
        }

        this.editableTabsValue = activeName;
        this.editableTabs = tabs.filter(tab => tab.name !== targetName);
      },
      async homemenuQuery() {
        const response = await Request.GET('/home/menu_query')
        if (response && response.data) {
          var data = response.data
          if (data.success) {
            this.$message.success(data.msg);
            this.menuData = data.data
          } else {
            this.$message.error(data.msg);
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
