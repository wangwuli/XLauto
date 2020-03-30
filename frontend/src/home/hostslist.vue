<template>
  <el-drawer
  title="target!!!"
  :visible.sync="drawer"
  :direction="direction"
  :before-close="handleClose"
  :style="{width: clientW + 'px'}">
    <el-row>
    <el-button icon="el-icon-d-arrow-right" circle style="float:right" @click="littleRight"></el-button>
    <el-button icon="el-icon-d-arrow-left" circle style="float:left" @click="littleLeft"></el-button>
    </el-row>
    <el-form ref="hostFilterform" :model="host_filter_form" label-width="80px" size="mini" style="padding-left: 15px;padding-top: 15px"
             :inline="true">
      <el-form-item size="mini" label="选择项目">
        <el-select v-model="host_filter_form.host_project" placeholder="请选择" size="mini">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item size="mini" label="选择类型">
        <el-select v-model="host_filter_form.host_type" placeholder="请选择" size="mini">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item size="mini" label="主机IP">
        <el-select v-model="host_filter_form.host_ip" placeholder="请选择" size="mini">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </el-form-item>
    </el-form>
  <el-table
    size="mini"
    ref="multipleTable"
    :data="tableData"
    tooltip-effect="dark"
    style="width: 100%; height:50%"
    @selection-change="handleSelectionChange">
    <el-table-column
      type="selection"
      width="55">
    </el-table-column>
    <el-table-column
      prop="host_ip"
      label="IP"
      width="120">
    </el-table-column>
    <el-table-column
      prop="type_name"
      label="主机类"
      width="120">
    </el-table-column>
    <el-table-column
      prop="host_name"
      label="主机名"
      show-overflow-tooltip>
    </el-table-column>
  </el-table>
  <el-pagination
    :size="mini"
    pager-count="3"
    @size-change="handleSizeChange"
    @current-change="handleCurrentChange"
    :current-page="currentPage4"
    :page-sizes="[100, 200, 300, 400]"
    :page-size="2"
    layout="total, sizes, pager"
    :small="true"
    :total="400">
  </el-pagination>
  </el-drawer>
</template>

<script>
import * as Request from '@/general/request.js'

export default {
  name: 'hostlist',
  data () {
    return {
      clientW: document.documentElement.clientWidth,
      host_filter_form: {
        host_project: '',
        host_type: '',
        host_ip: ''
      },
      drawer: false,
      direction: 'ltr',
      tableData: [],
      multipleSelection: [],
      value: '',
      options: [{
        value: '选项1',
        label: '黄金糕'
      }, {
        value: '选项2',
        label: '双皮奶'
      }, {
        value: '选项3',
        label: '蚵仔煎'
      }, {
        value: '选项4',
        label: '龙须面'
      }, {
        value: '选项5',
        label: '北京烤鸭'
      }]
    }
  },
  created () {
    this.hostslistQuery()
  },
  methods: {
    littleLeft () {
      this.clientW -= this.clientW * 0.2
    },
    littleRight () {
      this.clientW += this.clientW * 0.2
    },
    open_close (value) {
      this.drawer = value
    },
    handleClose (done) {
      done()
    },
    toggleSelection (rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row)
        })
      } else {
        this.$refs.multipleTable.clearSelection()
      }
    },
    handleSelectionChange (val) {
      this.multipleSelection = val
    },
    async hostslistQuery () {
      const response = await Request.GET('/home/hosts_query')
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.$message.success(data.msg)
          this.tableData = data.data
        } else {
          this.$message.error(data.msg)
        }
      }
    }
  }
}
</script>

<style scoped>

</style>
