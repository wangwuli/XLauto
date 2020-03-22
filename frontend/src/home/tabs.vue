<template>
    <div class=''>
        <el-tabs v-model="editableTabsValue" type="card" closable @tab-remove="removeTab" @tab-click="tabClick($event)">
            <el-tab-pane
                :key="item.name"
                v-for="item in editableTabs"
                :label="item.title"
                :name="item.name"
            >
            </el-tab-pane>
        </el-tabs>
        <router-view/> <!-- 放入router-view -->
    </div>
</template>

<script>
export default {
  name: 'tabs',
  components: {},
  data () {
    return {
    }
  },
  computed: {
    // 监听vuex保存的数据
    editableTabs: {
      get () {
        return this.$store.state.tabsPage
      },
      set (val) {
        this.$store.state.tabsPage = val
      }
    },
    editableTabsValue: {
      get () {
        return this.$store.state.TabsValue
      },
      set (val) {
        this.$store.state.TabsValue = val
      }
    }
  },
  methods: {
    removeTab (targetName) {
      var tabs = this.editableTabs
      var activeName = this.editableTabsValue
      if (activeName === targetName) {
        tabs.forEach((tab, index) => {
          if (tab.name === targetName) {
            var nextTab = tabs[index + 1] || tabs[index - 1]
            console.log(nextTab)
            if (nextTab) {
              activeName = nextTab.name
            }
          }
        })
      }
      this.editableTabsValue = activeName
      this.editableTabs = tabs.filter(tab => tab.name !== targetName)
      // 删除时跳转不在停留被删除页
      this.$router.push({ name: activeName })
    },
    // 已打开tabs切换事件
    tabClick (event) {
      this.$router.push({ name: event.name })
    }
  }
}
</script>

<!--// thanks https://www.jianshu.com/p/c0e3028ae378-->
