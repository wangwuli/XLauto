<template>
  <el-row>
    <div
      ref="dragIcon"
      class="dragIcon"
      @touchstart.stop="loghandleTouchStart"
      @touchmove.prevent.stop="loghandleTouchMove($event)"
      @touchend.stop="loghandleTouchEnd"
      :style="{left: left + 'px',top: top + 'px',width: itemWidth + 'px',height: itemHeight + 'px'}"
      v-if="isShow">
      <el-button type="info" @click="openlogDrawer" icon="el-icon-question" circle/>
    </div>
    <allDrawer ref="alldrawerref"></allDrawer>
    <div
      ref="host_dragIcon"
      class="dragIcon"
      @touchstart.stop="hosthandleTouchStart"
      @touchmove.prevent.stop="hosthandleTouchMove($event)"
      @touchend.stop="hosthandleTouchEnd"
      :style="{left: host_left + 'px',top: host_top + 'px',width: itemWidth + 'px',height: itemHeight + 'px'}"
      v-if="isShow">
    <el-button type="info" @click="openhostDrawer" icon="el-icon-aim" circle/>
  </div>
  <hostsList ref="hostlistref"></hostsList>
  </el-row>
</template>

<script>
import allDrawer from '@/home/alldrawer'
import hostsList from '@/home/hostslist'

export default {
  name: 'upperbutton',
  components: {
    allDrawer: allDrawer,
    hostsList: hostsList
  },
  props: {
    itemWidth: {
      type: Number,
      default: 40
    },
    itemHeight: {
      type: Number,
      default: 40
    }
  },
  data () {
    return {
      host_left: 0,
      host_top: 0,
      left: 0,
      top: 0,
      startToMove: false,
      isShow: true,
      timer: null,
      currentTop: null,
      clientW: document.documentElement.clientWidth, // 视口宽
      clientH: document.documentElement.clientHeight // 视口高
    }
  },
  created () {
    this.host_left = 30
    this.host_top = (this.clientH / 2 - this.itemHeight / 2)
    this.left = (this.clientW - this.itemWidth - 30)
    this.top = (this.clientH / 2 - this.itemHeight / 2)
  },
  mounted () {
    const that = this
    window.onresize = () => {
      return (() => {
        // debugger
        that.left = window.innerWidth - 15
        that.top = Math.floor(window.innerHeight / 2)
        that.host_left = -25
        that.host_top = that.top
      })()
    }
    // this.bindScrollEvent()
  },
  beforeDestroy () {
    // 记得销毁一些全局的的事件
    this.removeScrollEvent()
  },
  methods: {
    openhostDrawer () {
      this.$nextTick(() => {
        this.$refs.hostlistref.open_close(true)
      })
    },
    openlogDrawer () {
      this.$nextTick(() => {
        this.$refs.alldrawerref.open_close(true)
      })
    },
    loghandleTouchStart () {
      this.handleTouchStart()
      this.$refs.dragIcon.style.transition = 'none'
    },
    hosthandleTouchStart () {
      this.handleTouchStart()
      this.$refs.host_dragIcon.style.transition = 'none'
    },
    handleTouchStart () {
      this.startToMove = true
    },
    hosthandleTouchMove (e) {
      const clientX = e.targetTouches[0].clientX // 手指相对视口的x
      const clientY = e.targetTouches[0].clientY // 手指相对视口的y
      const isInScreen = clientX <= this.clientW && clientX >= 0 && clientY <= this.clientH && clientY >= 0
      if (this.startToMove && e.targetTouches.length === 1) {
        if (isInScreen) {
          this.host_left = clientX - this.itemWidth / 2
          this.host_top = clientY - this.itemHeight / 2
        }
      }
    },
    loghandleTouchMove (e) {
      const clientX = e.targetTouches[0].clientX // 手指相对视口的x
      const clientY = e.targetTouches[0].clientY // 手指相对视口的y
      const isInScreen = clientX <= this.clientW && clientX >= 0 && clientY <= this.clientH && clientY >= 0
      if (this.startToMove && e.targetTouches.length === 1) {
        if (isInScreen) {
          this.left = clientX - this.itemWidth / 2
          this.top = clientY - this.itemHeight / 2
        }
      }
    },
    loghandleTouchEnd () {
      // if (this.left < (this.clientW / 2)) {
      if (this.left > -20 && this.left < 0) {
        this.left = -20 // 不让贴边 所以设置30没设置0
        this.handleIconY()
      } else if (this.left < this.clientW && this.left > this.clientW - 40) {
        // this.left = this.clientW - this.itemWidth - 30 // 不让贴边 所以减30
        this.left = this.clientW - 20
        this.handleIconY()
        // this.left = document.documentElement.clientWidth - 25
      }
      this.$refs.dragIcon.style.transition = 'all .3s'
    },
    hosthandleTouchEnd () {
      // if (this.left < (this.clientW / 2)) {
      if (this.host_left > -20 && this.host_left < 0) {
        this.host_left = -20 // 不让贴边 所以设置30没设置0
        this.handleIconY()
      } else if (this.host_left < this.clientW && this.host_left > this.clientW - 40) {
        // this.left = this.clientW - this.itemWidth - 30 // 不让贴边 所以减30
        this.host_left = this.clientW - 20
        this.handleIconY()
        // this.left = document.documentElement.clientWidth - 25
      }
      this.$refs.host_dragIcon.style.transition = 'all .3s'
    },
    handleIconY () {
      if (this.top < 0) {
        this.top = 30 // 不上帖上边所以设置为30 没设置0
      } else if (this.top + this.itemHeight > this.clientH) {
        this.top = this.clientH - this.itemHeight - 30 // 不让帖下边所以减30
      }
    },
    bindScrollEvent () {
      window.addEventListener('scroll', this.handleScrollStart)
    },
    removeScrollEvent () {
      window.removeEventListener('scroll', this.handleScrollStart)
    },
    handleScrollStart () {
      this.isShow = false
      this.timer && clearTimeout(this.timer)
      this.timer = setTimeout(() => {
        this.handleScrollEnd()
      }, 300)
      this.currentTop = document.documentElement.scrollTop || document.body.scrollTop
    },
    handleScrollEnd () {
      this.scrollTop = document.documentElement.scrollTop || document.body.scrollTop
      // 判断是否停止滚动的条件
      if (this.scrollTop === this.currentTop) {
        this.isShow = true
      }
    }
  }
}
</script>

<style scoped>
  .dragIcon {
    position: fixed;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    /*background-color: #909399;*/
    /*line-height: 40px;*/
    text-align: center;
    color: #fff;
  }

  .v-enter {
    opacity: 1;
  }

  .v-leave-to {
    opacity: 0;
  }

  .v-enter-active,
  .v-leave-active {
    transition: opacity 0.3s;
  }
</style>
