<template>
  <el-row>

        <el-button v-text="ip_addr" size="mini" style="margin-right: 20px" @input="initWebSocket"></el-button>
        <el-radio v-model="radio" label="2" @change="if_stop_flush">停止刷新</el-radio>
        <el-radio v-model="radio" label="1" @change="if_stop_flush">定时刷新</el-radio>
        <span>间隔：</span>
        <el-input v-model="flush_time" placeholder="刷新" style="width: 5%;  margin-right: 20px" size="mini" @input="restart_ful_time"></el-input>
        <span>连接状态：</span>
        <i class="el-icon-success" v-if="status_colour" style="color:#91c7ae;"></i>
        <i class="el-icon-error" v-else  style="color:#c23531;"></i>
        <el-divider size="mini"></el-divider>
        <div style="float:left; height: 410px; width: 410px;">
          <div class="box-card-g">
          <el-card class="box-card">
            <div slot="header">
              <span>服务器时间</span>
            </div>
            <div v-html="monitoring_data.server_current_time" style="height: 10px">
            </div>
          </el-card>
          <el-card class="box-card" style="margin-top: 20px">
            <div slot="header">
              <span>当前登录用户数</span>
            </div>
            <div v-html="monitoring_data.login_user_number" style="height: 10px">
            </div>
          </el-card>
          </div>
          <div id="mem_show" class="chart-container grid-content"></div>
          <div id="mem_ta_show" class="chart-container grid-content"></div>
          <div id="mem_virtual_show" class="chart-container grid-content"></div>
        </div>
          <div id="disk_show" class="chart-container grid-content" style="height: 410px; width: 405px;"></div>
          <div id="cpu_loadaverage_show" class="chart-container grid-content" style="width: 405px;"></div>
          <div id="connect_show" class="chart-container grid-content" style="width: 405px;"></div>

    </el-row>
</template>
<script>
import Echarts from 'echarts'
import dark from '../../plugins/dark.json'
import { mapState } from 'vuex'
// import * as Request from '@/general/request.js'

export default {
  // name: 'host_m',
  data () {
    return {
      is_setInterval: '',
      status_colour: false,
      ip_addr: '未选择',
      radio: '1',
      flush_time: 15,
      monitoring_data: {
        login_user_number: 0,
        server_current_time: '未知',
        server_start_time: '未知'
      },
      mem_ta_option: {
        title: {
          text: '内存'
        },
        xAxis: {
          type: 'category',
          data: ['可使用'],
          show: true,
          max: 0
        },
        yAxis: {
          type: 'value',
          max: 0
        },
        grid: {
          left: 60
        },
        series: [{
          itemStyle: {
            normal: {
              color: '#91c7ae'
            }
          },
          radius: '50%',
          barWidth: 30,
          data: [0],
          type: 'bar',
          showBackground: true,
          backgroundStyle: {
            color: 'rgba(220, 220, 220, 0.8)'
          }
        }]
      },
      mem_virtual_option: {
        title: {
          text: '虚拟内存'
        },
        xAxis: {
          type: 'category',
          data: ['已使用'],
          show: true,
          max: 0
        },
        yAxis: {
          type: 'value',
          max: 0
        },
        grid: {
          left: 60
        },
        series: [{
          itemStyle: {
            normal: {
              color: '#c23531'
            }
          },
          radius: '50%',
          barWidth: 30,
          data: [0],
          type: 'bar',
          showBackground: true,
          backgroundStyle: {
            color: 'rgba(220, 220, 220, 0.8)'
          }
        }]
      },
      mem_option: {
        title: {
          text: '内存'
        },
        tooltip: {
          trigger: 'item',
          formatter: '{c}M'
        },
        series: [
          {
            itemStyle: {
              normal: { // 每个柱子的颜色即为colorList数组里的每一项，如果柱子数目多于colorList的长度，则柱子颜色循环使用该数组
                color: function (params) {
                  var colorList = ['#dd6b66', '#eedd78', '#8dc1a9', '#73a373']
                  return colorList[params.dataIndex]
                }
              }
            },
            name: '访问来源',
            type: 'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: false,
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '30',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: [
              { value: 0, name: '使用' },
              { value: 0, name: '共享' },
              { value: 0, name: '缓存缓冲' },
              { value: 0, name: '空闲' }
            ]
            // data: [
            //   { value: 335, name: '使用', itemStyle: { color: '#c23531' } },
            //   { value: 310, name: '共享', itemStyle: { color: '#f5e8c8' } },
            //   { value: 234, name: '缓存缓冲', itemStyle: { color: '#b8d2c7' } },
            //   { value: 1548, name: '空闲', itemStyle: { color: '#91c7ae' } }
            // ]
          }
        ]
      },
      disk_option: {
        title: {
          text: '硬盘'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: { // 坐标轴指示器，坐标轴触发有效
            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
          }
        },
        legend: {
          data: ['剩余(M)', '使用(M)']
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'value'
          }
        ],
        yAxis: [
          {
            type: 'category',
            axisTick: {
              show: false
            },
            data: ['未知']
          }
        ],
        series: [
          {
            itemStyle: {
              normal: {
                color: '#8dc1a9'
              }
              // normal: { // 每个柱子的颜色即为colorList数组里的每一项，如果柱子数目多于colorList的长度，则柱子颜色循环使用该数组
              //   color: function (params) {
              //     var colorList = ['#c23531']
              //     return colorList[params.dataIndex]
              //   }
              // }
            },
            name: '剩余(M)',
            type: 'bar',
            stack: '总量',
            label: {
              show: true,
              position: 'top'
            },
            data: [-1]
          },
          {
            itemStyle: {
              normal: {
                color: '#dd6b66'
              }
            },
            name: '使用(M)',
            type: 'bar',
            stack: '总量',
            label: {
              show: true,
              position: 'insideTop'
            },
            data: [1]
          }
        ]
      },
      cpu_loadaverage_option: {
        title: {
          text: 'CPU'
        },
        xAxis: {
          type: 'category',
          data: ['一分钟前', '五分钟前', '十分钟前']
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: [-1, -1, -1],
          type: 'line'
        }]
      },
      connect_option: {
        title: {
          text: 'TCP'
        },
        xAxis: {
          type: 'category',
          data: []
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: [],
          type: 'bar',
          showBackground: true,
          backgroundStyle: {
            color: 'rgba(220, 220, 220, 0.8)'
          }
        }]
      }
    }
  },
  destroyed () {
    this.websock.close()
  },
  mounted () {
    this.$nextTick(() => {
      this.initWebSocket()
      this.is_setInterval = setInterval(this.websocketonopen, this.flush_time * 1000)
      Echarts.registerTheme('dark', dark)
      this.pieCharts2 = Echarts.init(document.getElementById('mem_show', 'dark'))
      this.pieCharts2.setOption(this.mem_option)
      this.pieCharts = Echarts.init(document.getElementById('mem_ta_show', 'dark'))
      this.pieCharts.setOption(this.mem_ta_option)
      this.pieCharts3 = Echarts.init(document.getElementById('disk_show', 'dark'))
      this.pieCharts3.setOption(this.disk_option)
      this.pieCharts4 = Echarts.init(document.getElementById('cpu_loadaverage_show', 'dark'))
      this.pieCharts4.setOption(this.cpu_loadaverage_option)
      this.pieCharts5 = Echarts.init(document.getElementById('mem_virtual_show', 'dark'))
      this.pieCharts5.setOption(this.mem_virtual_option)
      this.pieCharts6 = Echarts.init(document.getElementById('connect_show', 'dark'))
      this.pieCharts6.setOption(this.connect_option)
      // window.addEventListener('resize', this.handleResize)
    })
  },
  methods: {
    stop_flush () {
      clearInterval(this.is_setInterval)
    },
    start_fulsh () {
      clearInterval(this.is_setInterval)
      this.is_setInterval = setInterval(this.websocketonopen, this.flush_time * 1000)
    },
    if_stop_flush () {
      if (this.radio === '2') {
        this.stop_flush()
      } else {
        this.start_fulsh()
      }
    },
    restart_ful_time () {
      this.if_stop_flush()
      // clearInterval(this.is_setInterval)
      // this.is_setInterval = setInterval(this.websocketonopen, this.flush_time * 1000)
    },
    // 初始化weosocket https://www.jianshu.com/p/9d8b2e42328c
    initWebSocket () {
      const wsuri = 'ws://localhost:5000/socket/hosts/info_query'
      this.websock = new WebSocket(wsuri)
      this.websock.onmessage = this.websocketonmessage
      this.websock.onopen = this.websocketonopen
      this.websock.onerror = this.websocketonerror
      this.websock.onclose = this.websocketclose
    },
    websocketonopen () { // 连接建立之后执行send方法发送数据
      var value = this.table_click_value
      if (value === '') {
        return false
      }
      if (this.websock.readyState === 3) {
        this.$message.warning('连接意外关闭,正在重连')
        this.initWebSocket()
      }
      this.ip_addr = value.host_ip
      var actions = { host_id: value.host_id, flush_time: this.flush_time }
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
        this.status_colour = true
      } else {
        this.$message.error(data.msg)
        this.status_colour = false
      }
    },
    websocketsend (Data) { // 数据发送
      this.websock.send(Data)
    },
    websocketclose (e) { // 关闭
      console.log('断开连接', e)
    },
    datassetOption (data) {
      var usepartitionSizelist = []
      var surplusPartitionsize = []
      var mountPartitiondir = []
      for (var key in data.hard_disk) {
        var item = data.hard_disk[key]
        usepartitionSizelist.push(item.use_partition_size)
        surplusPartitionsize.push(item.surplus_partition_size)
        mountPartitiondir.push(item.mount_partition_dir)
      }
      // console.log(data.hard_disk)
      this.cpu_loadaverage_option.series[0].data = data.cpu_loadaverage
      this.disk_option.series[0].data = surplusPartitionsize
      this.disk_option.series[1].data = usepartitionSizelist
      this.disk_option.yAxis[0].data = mountPartitiondir
      this.monitoring_data.login_user_number = data.login_user_number
      this.monitoring_data.server_current_time = data.server_current_time
      this.monitoring_data.server_start_time = data.server_start_time
      this.mem_option.series[0].data[0].value = data.mem_used
      this.mem_option.series[0].data[1].value = data.mem_shared
      this.mem_option.series[0].data[2].value = data.mem_buffcache
      this.mem_option.series[0].data[3].value = data.mem_free
      this.mem_ta_option.yAxis.max = data.mem_total
      this.mem_ta_option.series[0].data[0] = data.mem_available
      this.mem_virtual_option.yAxis.max = data.swap_total
      this.mem_virtual_option.series[0].data[0] = data.swap_used
      this.connect_option.xAxis.data = data.socket_tu_name
      this.connect_option.series[0].data = data.socket_tu_value

      this.pieChartssetOption()
    },
    pieChartssetOption () {
      this.pieCharts.setOption(this.mem_ta_option)
      this.pieCharts2.setOption(this.mem_option)
      this.pieCharts3.setOption(this.disk_option)
      this.pieCharts4.setOption(this.cpu_loadaverage_option)
      this.pieCharts5.setOption(this.mem_virtual_option)
      this.pieCharts6.setOption(this.connect_option)
    }
    // async hostinfoQuery () {
    //   var value = this.table_click_value
    //   if (value === '') {
    //     return false
    //   }
    //   this.ip_addr = value.host_ip
    //   const response = await Request.GET('/hosts/info_query', value)
    //   if (response && response.data) {
    //     var data = response.data
    //     if (data.success) {
    //       this.$message.success(data.msg)
    //       this.datassetOption(data.data)
    //       this.status_colour = true
    //     } else {
    //       this.$message.error(data.msg)
    //       this.status_colour = false
    //     }
    //   }
    // }
  },
  computed: {
    ...mapState({
      table_click_value: 'host_table_click_value'
    })
  }
}
</script>
<style scoped>
.chart-container {
  /*border-radius: 4px;*/
  height: 200px;
  width: 200px;
  /*background: #fff;*/
  box-shadow: 0 1px 10px 2px rgba(182, 191, 196, 0.5);
  /*padding: 20px;*/
  float:left;
  margin : 0px 0px 5px 5px;
}

.box-card-g {
  height: 200px;
  width: 200px;
  float:left;
  margin : 0px 1px 0px 4px;
  box-shadow: 0 1px 10px 2px rgba(182, 191, 196, 0.5);
}

.box-card {
  font-size: 10px;
  width: 200px;
  float:left;
  /*margin : 0px 2px 0px 2px;*/
  /*box-shadow: 0 1px 10px 2px rgba(182, 191, 196, 0.5);*/
}

.grid-content {
    border-radius: 4px;
    min-height: 36px;
  }

/*.el-card /deep/ .el-card__body {*/
/*  margin-top:-3px;*/
/*}*/

.el-card /deep/ .el-card__header {
    padding: 8px 20px;
    border-bottom: 1px solid #4b565b;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    font-size: 16px;
    background-color: #ccc;
}

.el-divider--horizontal {
  margin: 10px 0;
}

</style>
