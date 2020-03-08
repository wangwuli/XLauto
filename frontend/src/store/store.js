import Vue from 'vue';
import Vuex from 'vuex';
// 引入 router 在vuex内使用router跳转
import router from '../router/index.js';

Vue.use(Vuex);
Vue.use(router);

export default new Vuex.Store({
  state: { // 定义tabs 所需参数
    tabsPage: [],
    TabsValue: ''
  },
  mutations: {
    editableTabs: (state, obj) => {
      obj = obj.entity
      debugger
      // 浅拷贝 store.tabsPage
      let arr = Array.from(state.tabsPage);
      // 判断数组内是否为空
      if (arr.length !== 0) {
        // 使用 Array.some 去判断是否存在对象信息
        var even = function (obj) {
          return arr.some(item => {
            return item.name === obj.name;
          });
        };
        // even方法 如果对象存在返回true,不存在则返回flase
        // 加！触发 true 代码块
        if (!even(obj)/* 如果不存在将对象push进数组内bing */) {
          // 将tabs所需参数push进arr数组
          arr.push({title: obj.title, name: obj.name});
          // 赋值给tabsPage参数
          state.tabsPage = arr;
          // 赋值给TabsValue参数
          state.TabsValue = obj.name;
          // 跳转
          // router.push({name: obj.name});
        } else { // 如果存在 只做跳转选中
          // 赋值给TabsValue参数
          state.TabsValue = obj.name;
          // 跳转
          // router.push({name: obj.name});
        }
        ;
      } else {// 如果为0
        // 将tabs所需参数push进arr数组
        arr.push({
          title: obj.title, name: obj.name
        });
        // 赋值给tabsPage参数
        state.tabsPage = arr;
        // 赋值给TabsValue参数
        state.TabsValue = obj.name;
        // 跳转
        // router.push({name: obj.name});
      }
    }
  },
  actions: {
    // 注册方法
    editableTabs(context, obj) {
      context.commit('editableTabs', obj);
    }
  }
});

// thanks https://www.jianshu.com/p/c0e3028ae378
