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
      title="我是标题"
      :visible.sync="drawer"
      :direction="direction"
      :before-close="handleClose">
      <span>我来啦!</span>
    </el-drawer>
<!--  </el-row>-->
</template>

<script>
export default {
  name: 'alldrawer',
  data () {
    return {
      drawer: true,
      direction: 'rtl'
    }
  },
  methods: {
    open_close (value) {
      this.drawer = value
    },
    handleClose (done) {
      this.$confirm('确认关闭？')
        .then(_ => {
          done()
        })
        .catch(_ => {})
    }
  }
}
</script>
