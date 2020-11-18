<template>
  <el-row>
    <el-button type="primary" size="mini" @click="open_big_file_dialog">查询大文件</el-button>
    <el-row>
  <el-table
    :row-style="{height:'20px'}"
    :cell-style="{padding:'0px'}"
    style="font-size: 10px;width: 100%"
    size="mini"
    :data="tableData"
    :row-class-name="tableRowClassName"
    @selection-change="handleSelectionChange">
    <el-table-column
      type="selection"
      width="55">
    </el-table-column>
    <el-table-column
      prop="date"
      label="日期"
      width="180">
    </el-table-column>
    <el-table-column
      prop="name"
      label="姓名"
      width="180">
    </el-table-column>
    <el-table-column
      prop="address"
      label="地址"
    show-overflow-tooltip>
    </el-table-column>
    <el-table-column
      fixed="right"
      label="操作"
      width="100">
      <template slot-scope="scope">
        <el-button @click="handleClick(scope.row)" type="text" size="small">部署</el-button>
        <el-button type="text" size="small">重启</el-button>
      </template>
    </el-table-column>
  </el-table>
    </el-row>
    <el-row>
      <querybigfileDialog :visible.sync="dialogq_bigfile_on_close" v-if="dialogq_bigfile_on_close"></querybigfileDialog>
    </el-row>
  </el-row>
</template>

<script>
import querybigfileDialog from '@/components/host_m/hots_common_el/query_big_file'

export default {
  data () {
    return {
      dialogq_bigfile_on_close: false,
      tableData: [{
        date: '2016-05-01',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }]
    }
  },
  components: {
    querybigfileDialog: querybigfileDialog
  },
  methods: {
    open_big_file_dialog () {
      this.dialogq_bigfile_on_close = true
    },
    tableRowClassName ({ row, rowIndex }) {
      if (rowIndex === 1) {
        return 'warning-row'
      }
      return ''
    }
  }
}
</script>
<style>
  .el-table .warning-row {
    background: oldlace;
  }

  .el-table .success-row {
    background: #f0f9eb;
  }
</style>
