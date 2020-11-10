<template>
<el-dialog title="收货地址" :visible.sync="dialogq_bigfile">
  <el-table :data="gridData">
    <el-table-column property="date" label="日期" width="150"></el-table-column>
    <el-table-column property="name" label="姓名" width="200"></el-table-column>
    <el-table-column property="address" label="地址"></el-table-column>
  </el-table>
</el-dialog>
</template>

<script>
export default {
  name: 'zabbix',
  data () {
    return {
      dialogq_bigfile: false
    }
  }
}
</script>

<style scoped>

</style>
