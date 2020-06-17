<template>
  <el-row>
    <el-drawer
      title="What happened?"
      :visible.sync="drawer"
      :direction="direction"
      :before-close="handleClose">
      <el-tooltip class="item" effect="dark" content="开始收集" placement="top-start">
        <el-button type="primary" size="mini" icon="el-icon-edit" @click="" circle></el-button>
      </el-tooltip>
      <el-tooltip class="item" effect="dark" content="清空此次收集" placement="top-start">
        <el-button type="danger" size="mini" icon="el-icon-delete" circle></el-button>
      </el-tooltip>
      <el-input
        :rows="textarea_rows"
        type="textarea"
        placeholder="未显示内容"
        v-model="happened_text">
      </el-input>
    </el-drawer>
  </el-row>
</template>

<script>
import { mapState } from 'vuex'

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
  computed: {
    ...mapState({
      background_socket: 'background_socket'
    })
  },
  methods: {
    open_close (value) {
      this.drawer = value
    },
    handleClose (done) {
      done()
    },
    start_collection () {
      this.initWebSocket()
    },
    end_llection () {
      this.initWebSocket()
    },
    datassetOption (data) {
      this.happened_text += data
    },
    initWebSocket () {
      const wsuri = 'ws://' + this.background_socket + '/socket/log/happened'
      this.websock = new WebSocket(wsuri)
      this.websock.onmessage = this.websocketonmessage
      this.websock.onopen = this.websocketonopen
      this.websock.onerror = this.websocketonerror
      this.websock.onclose = this.websocketclose
    },
    websocketonopen () { // 连接建立之后执行send方法发送数据
      var actions = { starttime: '', endtime: '' }
      this.websocketsend(JSON.stringify(actions))
    },
    websocketonerror () { // 连接建立失败重连
      this.initWebSocket()
    },
    websocketonmessage (e) { // 数据接收
      const data = JSON.parse(e.data)
      if (data.success) {
        this.$message.success(data.msg)
        this.datassetOption(data.data)
      } else {
        this.$message.error(data.msg)
      }
    },
    websocketsend (Data) { // 数据发送
      this.websock.send(Data)
    },
    websocketclose (e) { // 关闭
      console.log('断开连接', e)
    }
  }
}
</script>

<style scoped>
  /*.textarea >>> .el-textarea__inner {*/
  /*  height: 100px; !important;*/
  /*}*/
</style>
