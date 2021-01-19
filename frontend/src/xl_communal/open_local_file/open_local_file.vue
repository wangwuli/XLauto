<template>
  <el-row>
    <el-table
      @current-change="handleCurrentChange"
      highlight-current-row
      :row-style="{height:'20px'}"
      :cell-style="{padding:'0px'}"
      size="mini"
      :data="soft_table_data"
      style="width: 80%">
      <el-table-column
        type="index"
        width="50">
      </el-table-column>
      <el-table-column
        prop="software_name"
        label="软件">
      </el-table-column>
      <el-table-column
        prop="software_versions"
        label="版本">
      </el-table-column>
    </el-table>
  </el-row>
</template>

<script>
export default {
  data () {
    return {
      soft_table_data: ''
    }
  },
  name: 'open_local_file',
  props: {
    software_package_id: {
      type: Number,
      default: null
    }
  }
}
</script>

<style scoped>

</style>
