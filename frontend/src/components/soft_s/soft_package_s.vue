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
    <el-dialog title="包上传" :visible.sync="adddialog" width="610px">
      <el-form :model="software_package_form" ref="software_package_form_ref" :rules="rules" size="mini" :inline="true" style="margin-top: 20px">
          <el-form-item label="软件名称" prop="software_name">
            <el-input
              placeholder="请输入内容"
              v-model="software_package_form.software_name"
              clearable>
            </el-input>
          </el-form-item>
          <el-form-item label="软件版本"  prop="software_versions">
            <el-input
              placeholder="请输入内容"
              v-model="software_package_form.software_versions"
              clearable>
            </el-input>
          </el-form-item>
          <el-form-item label="安装方式"  prop="software_install_type">
            <el-select v-model="software_package_form.software_install_type" placeholder="请选择">
              <el-option
                v-for="item in software_install_type"
                :key="item.code_key"
                :label="item.code_name"
                :value="item.code_key">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="压缩方式"  prop="software_package_zip_type">
            <el-select v-model="software_package_form.software_package_zip_type" placeholder="请选择">
              <el-option
                v-for="item in software_package_zip_type"
                :key="item.code_key"
                :label="item.code_name"
                :value="item.code_key">
              </el-option>
            </el-select>
          </el-form-item>
      </el-form>
      <el-upload
        :data="software_package_form"
        drag
        multiple
        accept=".zip,.gz,.tgz,.tar"
        :limit="1"
        class="upload-demo"
        ref="upload"
        action="/deploy/soft_package"
        :on-preview="handlePreview"
        :on-remove="handleRemove"
        :file-list="fileList"
        :auto-upload="false">
        <div slot="tip" class="el-upload__tip">只能上传zip/gz/tgz/tar文件，且只能一个</div>
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      </el-upload>
      <el-button style="margin-right: 10px;margin-bottom: 10px; float: right" size="mini" type="success"
                 @click="submitUpload">提交
      </el-button>
    </el-dialog>
  </el-row>
</template>

<script>
import * as Request from '@/general/request.js'
export default {
  name: 'zabbix',
  created () {
    this.software_package_zip_type_query()
    this.software_install_type_query()
  },
  methods: {
    handleClick (response) {
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.$message.success(data.msg)
          this.adddialog = false
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    submitUpload () {
      this.$refs.software_package_form_ref.validate((valid) => {
        if (valid) {
          this.$refs.upload.submit()
        } else {
          return false
        }
      })
    },
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePreview (file) {
      console.log(file)
    },
    async software_package_zip_type_query () {
      const response = await Request.GET('/general/code_query', { code_type: 'software_package_zip_type' })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          // this.$message.success(data.msg)
          this.software_package_zip_type = data.data
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    async software_install_type_query () {
      const response = await Request.GET('/general/code_query', { code_type: 'software_install_type' })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          // this.$message.success(data.msg)
          this.software_install_type = data.data
        } else {
          this.$message.error(data.msg)
        }
      }
    }
  },
  data () {
    return {
      rules: {
        software_name: [
          { required: true, message: '请输入活动名称', trigger: 'blur' }
        ],
        software_versions: [
          { required: true, message: '请输入活动名称', trigger: 'blur' }
        ],
        software_package_zip_type: [
          { required: true, message: '请输入活动名称', trigger: 'blur' }
        ],
        software_install_type: [
          { required: true, message: '请输入活动名称', trigger: 'blur' }
        ]
      },
      software_package_form: {
        software_name: '',
        software_versions: '',
        software_package_zip_type: '',
        software_install_type: ''
      },
      software_install_type_value: '',
      software_install_type: [],
      software_package_zip_type_value: '',
      software_package_zip_type: [],
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
  /deep/ .el-upload-dragger {
    width: 553px;
    height: 130px;
  }
</style>
