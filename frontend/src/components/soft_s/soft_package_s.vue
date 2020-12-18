<template>
  <el-row>
    <el-button type="primary" size="mini" @click="adddialog = true">新增</el-button>
    <el-button type="danger" size="mini">删除</el-button>
    <el-table
      class="tableClass"
      :row-style="{height:'20px'}"
      :cell-style="{padding:'0px'}"
      height="250"
      size="mini"
      :data="tableData"
      stripe
      style="margin-left: 20px; width: 100%">
      <el-table-column
        type="selection">
      </el-table-column>
      <el-table-column
        show-overflow-tooltip
        fixed
        label="操作">
        <template slot-scope="scope">
          <el-button @click="handleClick(scope.row)" type="text" size="small">编辑</el-button>
        </template>
      </el-table-column>
      <el-table-column
        show-overflow-tooltip
        prop="date"
        label="软件名">
      </el-table-column>
      <el-table-column
        show-overflow-tooltip
        prop="name"
        label="包文件">
      </el-table-column>
      <el-table-column
        show-overflow-tooltip
        prop="province"
        label="版本">
      </el-table-column>
      <el-table-column
        show-overflow-tooltip
        prop="city"
        label="安装方式"
        width="120">
      </el-table-column>
      <el-table-column
        show-overflow-tooltip
        prop="address"
        label="配置文件">
      </el-table-column>
      <el-table-column
        show-overflow-tooltip
        prop="zip"
        label="备注">
      </el-table-column>
    </el-table>
    <el-dialog title="包上传" :visible.sync="adddialog">
           <el-upload
        drag
        multiple
        accept=".zip,.gz,.tgz,.tar"
        :limit="1"
        class="upload-demo"
        ref="upload"
        action="https://jsonplaceholder.typicode.com/posts/"
        :on-preview="handlePreview"
        :on-remove="handleRemove"
        :file-list="fileList"
        :auto-upload="false">
        <div slot="tip" class="el-upload__tip">只能上传zip/gz/tgz/tar文件，且只能一个</div>
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      </el-upload>
      <el-form :model="configuration_form" size="mini" :inline="true">
        <el-row>
          <el-form-item label="软件名称">
            <el-input
              placeholder="请输入内容"
              v-model="input"
              clearable>
            </el-input>
          </el-form-item>
          <el-form-item label="软件名称">
            <el-input
              placeholder="请输入内容"
              v-model="input"
              clearable>
            </el-input>
          </el-form-item>
          <el-form-item label="软件名称">
            <el-input
              placeholder="请输入内容"
              v-model="input"
              clearable>
            </el-input>
          </el-form-item>
          <el-form-item label="软件名称">
            <el-input
              placeholder="请输入内容"
              v-model="input"
              clearable>
            </el-input>
          </el-form-item>
        </el-row>
      </el-form>
      <el-button style="margin-right: 10px;margin-bottom: 10px; float: right" size="mini" type="success" @click="submitUpload">提交
      </el-button>
    </el-dialog>
  </el-row>
</template>

<script>
export default {
  name: 'zabbix',
  methods: {
    handleClick (row) {
      console.log(row)
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
  },
  data () {
    return {
      adddialog: false,
      tableData: [{
        date: '2016-05-02',
        name: '王小虎',
        province: '上海',
        city: '普陀区',
        address: '上海市普陀区金沙江路 1518 弄',
        zip: 200333
      }, {
        date: '2016-05-04',
        name: '王小虎',
        province: '上海',
        city: '普陀区',
        address: '上海市普陀区金沙江路 1517 弄',
        zip: 200333
      }, {
        date: '2016-05-01',
        name: '王小虎',
        province: '上海',
        city: '普陀区',
        address: '上海市普陀区金沙江路 1519 弄',
        zip: 200333
      }, {
        date: '2016-05-03',
        name: '王小虎',
        province: '上海',
        city: '普陀区',
        address: '上海市普陀区金沙江路 1516 弄',
        zip: 200333
      }]
    }
  }
}
</script>

<style scoped>
  /deep/ .el-table__fixed-right {
    height: 100% !important;
  }
  /deep/ .el-table__fixed {
    height: 100% !important;
  }
</style>
