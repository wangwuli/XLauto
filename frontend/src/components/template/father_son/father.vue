<template>
  <el-row>
    <el-button type="primary" size="mini" @click="open_big_file_dialog">查询大文件</el-button>
      <querybigfileDialog :visible.sync="dialogq_bigfile_on_close" v-if="dialogq_bigfile_on_close"></querybigfileDialog>
  </el-row>
</template>

<script>
import querybigfileDialog from './son'

export default {
  data () {
    return {
      dialogq_bigfile_on_close: false
    }
  },
  components: {
    querybigfileDialog: querybigfileDialog
  },
  methods: {
    open_big_file_dialog () {
      this.dialogq_bigfile_on_close = true
    }
  }
}
</script>
