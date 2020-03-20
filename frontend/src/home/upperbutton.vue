<template>
  <row>
    <dev
         ref="dragIcon"
         class="dragIcon"
         @touchstart.stop="handleTouchStart"
         @touchmove.prevent.stop="handleTouchMove($event)"
         @touchend.stop="handleTouchEnd"
         :style="{left: left + 'px',top: top + 'px',width: itemWidth + 'px',height: itemHeight + 'px'}"
         v-if="isShow">
      <el-button type="info" @click="openlogDrawer" icon="el-icon-question" circle></el-button>
    </dev>
    <allDrawer ref="alldrawerref" ></allDrawer>
  </row>
</template>

<script>
import allDrawer from '@/home/alldrawer'

export default {
  components: {
    allDrawer: allDrawer
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
      })()
    }
    // this.bindScrollEvent()
  },
  beforeDestroy () {
    // 记得销毁一些全局的的事件
    this.removeScrollEvent()
  },
  methods: {
    openlogDrawer () {
      this.$nextTick(() => {
        console.log(this.$refs.alldrawerref)
        this.$refs.alldrawerref.open_close(true)
      })
    },
    handleTouchStart () {
      this.startToMove = true
      this.$refs.dragIcon.style.transition = 'none'
    },
    handleTouchMove (e) {
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
    handleTouchEnd () {
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
    line-height: 40px;
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
