import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import HelloWorld from '@/components/HelloWorld'
import TEST from '@/components/TEST'

Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: Home
  // },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/network',
    name: 'network',
    component: HelloWorld
  },
  {
    path: '/test',
    name: 'test',
    component: TEST
  }
]

const router = new VueRouter({
  routes
})

export default router