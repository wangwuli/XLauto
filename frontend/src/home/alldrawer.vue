<template>
<!--  <el-row>-->
<!--    <el-radio-group v-model="direction">-->
<!--      <el-radio label="ltr">从左往右开</el-radio>-->
<!--      <el-radio label="rtl">从右往左开</el-radio>-->
<!--      <el-radio label="ttb">从上往下开</el-radio>-->
<!--      <el-radio label="btt">从下往上开</el-radio>-->
<!--    </el-radio-group>-->

<!--    <el-button @click="drawer = true" type="primary" style="margin-left: 16px;">-->
<!--      点我打开-->
<!--    </el-button>-->

    <el-drawer
      title="What happened?"
      :visible.sync="drawer"
      :direction="direction"
      :before-close="handleClose">
<!--      <span>我来啦!</span>-->
      <el-input
        :rows="textarea_rows"
        type="textarea"
        placeholder="请输入内容"
        v-model="happened_text">
      </el-input>
    </el-drawer>
<!--  </el-row>-->
</template>

<script>
export default {
  name: 'alldrawer',
  mounted () {
    const that = this
    window.onresize = () => {
      return (() => {
        // debugger
        that.screenheight = window.innerHeight
        if (that.screenheight > 150) {
          that.textarea_rows = Math.floor((that.screenheight - 80) / 24)
        } else {
          that.textarea_rows = 2
        }
      })()
    }
  },
  data () {
    return {
      textarea_rows: Math.floor((window.innerHeight - 80) / 24),
      screenheight: window.innerHeight,
      drawer: false,
      direction: 'rtl',
      happened_text: ''
    }
  },
  methods: {
    open_close (value) {
      this.drawer = value
    },
    handleClose (done) {
      done()
      // this.$confirm('确认关闭？')
      //   .then(_ => {
      //     done()
      //   })
      //   .catch(_ => {})
    }
  }
}
</script>

<style scoped>
  /*.textarea >>> .el-textarea__inner {*/
  /*  height: 100px; !important;*/
  /*}*/
</style>
