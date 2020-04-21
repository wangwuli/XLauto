<template>
  <el-row>
    <el-tabs :tab-position="tabPosition" style="height: 100%">
      <el-tab-pane label="主机信息">
        <div id="mem_show" class="chart-container"></div>
        <div id="mem_ta_show" class="chart-container"></div>
      </el-tab-pane>
      <el-tab-pane label="命令推送">配置管理</el-tab-pane>
      <el-tab-pane label="待开发">角色管理</el-tab-pane>
    </el-tabs>
  </el-row>
</template>
<script>
import Echarts from 'echarts'
export default {
  name: 'host_m',
  data () {
    return {
      tabPosition: 'left',
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
          max: 100000
        },
        grid: {
          left: 60
        },
        series: [{
          radius: '50%',
          barWidth: 30,
          data: [1000],
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
              { value: 335, name: '使用', itemStyle: { color: '#c23531' } },
              { value: 310, name: '共享', itemStyle: { color: '#f5e8c8' } },
              { value: 234, name: '缓存缓冲', itemStyle: { color: '#b8d2c7' } },
              { value: 1548, name: '空闲', itemStyle: { color: '#91c7ae' } }
            ]
          }
        ]
      }
    }
  },
  mounted () {
    this.$nextTick(() => {
      this.pieCharts2 = Echarts.init(document.getElementById('mem_show'))
      this.pieCharts2.setOption(this.mem_option)
      this.pieCharts = Echarts.init(document.getElementById('mem_ta_show'))
      this.pieCharts.setOption(this.mem_ta_option)

      // window.addEventListener('resize', this.handleResize)
    })
  },
  methods: {
    handleResize () {
      // this.pieCharts.resize()
    }
  },
  beforeDestroy () {
    // window.removeEventListener('resize', this.handleResize)
    // this.pieCharts.dispose()
  }
}
</script>
<style scoped>
.chart-container {
  border-radius: 4px;
  height: 200px;
  width: 200px;
  background: #fff;
  box-shadow: 0 1px 10px 2px rgba(182, 191, 196, 0.5);
  padding: 20px;
  float:left;
}
</style>
