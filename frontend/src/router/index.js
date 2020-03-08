import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import TEST from '@/components/TEST'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/network',
      name: 'network',
      component: HelloWorld
    }
    ,
    {
      path: '/test',
      name: 'test',
      component: TEST
    }
  ]
})
