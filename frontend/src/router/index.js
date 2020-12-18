import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import HelloWorld from '@/components/HelloWorld'
import HostM from '@/components/host_m/host_m'
import SoftD from '@/components/soft_m/soft_m'
import ZabbixM from '@/components/soft_m/zabbix/index'
import Setting from '@/components/setting/index'
import SoftS from '@/components/soft_s/soft_s'

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
    path: '/host_m',
    name: 'host_m',
    component: HostM
  },
  {
    path: '/soft_d',
    name: 'soft_d',
    component: SoftD
  },
  {
    path: '/zabbix',
    name: 'zabbix',
    component: ZabbixM
  },
  {
    path: '/setting',
    name: 'setting',
    component: Setting
  },
  {
    path: '/soft_s',
    name: 'soft_s',
    component: SoftS
  }
]

const router = new VueRouter({
  routes
})

export default router
