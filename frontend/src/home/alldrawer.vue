<template>
  <el-row>
    <el-drawer
      title="What happened?"
      :visible.sync="drawer"
      :direction="direction"
      :before-close="handleClose">
      <el-alert
        style="height: 25px"
        :closable="false"
        :title="log_info_text"
        :type="log_info_type"
        show-icon>
      </el-alert>
      <el-tooltip class="item button_location" effect="dark" content="开始收集" placement="top-start">
        <el-button type="primary" size="mini" icon="el-icon-video-camera-solid" @click="start_collection" circle></el-button>
      </el-tooltip>
      <el-tooltip class="item button_location" effect="dark" content="暂停收集" placement="top-start">
        <el-button type="danger" size="mini" icon="el-icon-delete" @click="end_llection"  circle></el-button>
      </el-tooltip>
      <!--<el-divider size="mini"></el-divider>-->
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
      log_info_text: '未开始',
      log_info_type: 'info',
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
      this.websock.close()
      this.log_info_type = 'warning'
      this.log_info_text = '收集停止'
      // this.websocketclose()
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
        // this.$message.success(data.msg)
        this.log_info_type = 'success'
        this.log_info_text = '正在收集'
        this.datassetOption(data.data)
      } else {
        this.$message.error(data.msg)
        this.log_info_type = 'error'
        this.log_info_text = '收集失败'
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
  .el-divider--horizontal {
    margin: 10px 0;
  }
  .button_location {
    margin: 6px;
  }
</style>
