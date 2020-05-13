<template>
  <el-row>
    <el-button type="primary" size="mini" @click="updatedialog = true">上传<i class="el-icon-upload el-icon--right"></i></el-button>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>已存脚本</span>
      </div>
      <el-table
      :data="tableData"
      style="width: 300px; height: 200px"
      size="mini">
      <el-table-column
        prop="date"
        label="脚本名"
        show-overflow-tooltip>
      </el-table-column>
      <el-table-column
        prop="name"
        label="类型"
        show-overflow-tooltip>
      </el-table-column>
      <el-table-column
        prop="address"
        label="备注"
      show-overflow-tooltip>
      </el-table-column>
    </el-table>
      </el-card>

    <el-dialog title="脚本上传" :visible.sync="updatedialog" class="update-dialog" width="500px" >
      <el-upload
        style="height: 200px"
        class="upload-demo"
        ref="uplo--color-primaryad"
        action="https://jsonplaceholder.typicode.com/posts/"
        :on-preview="handlePreview"
        :on-remove="handleRemove"
        :file-list="fileList"
        :auto-upload="false"
        accept=".sh"
        :limit = 3
        :on-exceed = "exceed_updte"
    >
      <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
      <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
      <div slot="tip" class="el-upload__tip">同时只能上传3个sh文件</div>
    </el-upload>
    </el-dialog>

  </el-row>
</template>
<script>
export default {
  data () {
    return {
      updatedialog: false,
      fileList: [
      ]
    }
  },
  methods: {
    exceed_updte () {
      this.$message.warning('最多只能上传3个脚本')
    },
    submitUpload () {
      this.$refs.upload.submit()
    },
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePreview (file) {
      console.log(file)
    }
  }
}
</script>

<style scoped>
  .box-card {
    width: 300px;
    height: 200px;
    font-size: 5px;
  }
  .update-dialog .el-dialog__body {
    width: 50px;
  }
   .el-card /deep/ .el-card__header {
    padding: 10px 20px;
  }

  .el-card /deep/ .el-card__body {
    padding: 0px;
  }
</style>
