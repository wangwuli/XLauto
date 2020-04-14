<template>
  <el-row>
    <el-tabs :tab-position="tabPosition" style="height: 100%">
      <el-tab-pane label="主机信息">
        <div id="pieChart" class="chart-container"></div>
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
      pieOption: {
        title: {
          text: '星级分布'
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b}: {c} ({d}%)'
        },
        series: [
          {
            name: '访问来源',
            type: 'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: true,
            label: {
              emphasis: {
                show: true,
                textStyle: {
                  fontSize: '30',
                  fontWeight: 'bold'
                }
              }
            },
            data: [
              { value: 335, name: '二星' },
              { value: 310, name: '三星' },
              { value: 234, name: '四星' },
              { value: 135, name: '五星' }
            ]
          }
        ]
      }
    }
  },
  mounted () {
    this.$nextTick(() => {
      this.pieCharts = Echarts.init(document.getElementById('pieChart'))
      this.pieCharts.setOption(this.pieOption)
      window.addEventListener('resize', this.handleResize)
    })
  },
  methods: {
    handleResize () {
      this.pieCharts.resize()
    }
  },
  beforeDestroy () {
    window.removeEventListener('resize', this.handleResize)
    this.pieCharts.dispose()
  }
}
</script>
<style scoped>
.chart-container {
  border-radius: 4px;
  height: 400px;
  background: #fff;
  box-shadow: 0 1px 10px 2px rgba(182, 191, 196, 0.5);
  padding: 20px;
}
</style>
