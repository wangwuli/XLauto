<template>
  <el-row>
    <el-button type="primary" size="mini" @click="adddialog = true">本地新增</el-button>
    <el-button type="danger" size="mini" @click="del_software_package_dialog = true">删除</el-button>
    <el-button type="primary" size="mini" @click="software_package_query">刷新</el-button>
    <el-table
      ref="tableData_ref"
      class="tableClass"
      :row-style="{height:'20px'}"
      :cell-style="{padding:'0px'}"
      :height="table_top"
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
        prop="software_name"
        label="软件名">
      </el-table-column>
      <el-table-column
        show-overflow-tooltip
        prop="package_path"
        label="包文件">
      </el-table-column>
      <el-table-column
        show-overflow-tooltip
        prop="software_versions"
        label="版本">
      </el-table-column>
      <el-table-column
        show-overflow-tooltip
        prop="package_storage_type_name"
        label="存储方式"
        width="120">
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
          <el-form-item label="存储方式"  prop="package_storage_type">
            <el-select v-model="software_package_form.package_storage_type" placeholder="请选择">
              <el-option
                v-for="item in package_storage_type"
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
        :on-success="updata_success"
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
    <el-dialog title="确认删除勾选包信息" :visible.sync="del_software_package_dialog" width="500px" >
      <div slot="footer" class="dialog-footer">
        <el-button @click="del_software_package_dialog = false" size="mini">取 消</el-button>
        <el-button type="primary" @click="software_package_del" size="mini">确 定</el-button>
      </div>
    </el-dialog>
  </el-row>
</template>

<script>
import * as Request from '@/general/request.js'
export default {
  name: 'zabbix',
  created () {
    this.software_package_zip_type_query()
    this.package_storage_type_query()
    this.software_package_query()
  },
  methods: {
    handleClick (response) {
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
    updata_success (response) {
      if (response.success) {
        this.$message.success(response.msg)
        this.adddialog = false
        this.software_package_query()
      } else {
        this.$message.error(response.msg)
      }
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
    async package_storage_type_query () {
      const response = await Request.GET('/general/code_one_query', { code_type: 'package_storage_type', code_key: 'local' })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          // this.$message.success(data.msg)
          this.package_storage_type = data.data
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    async software_package_query () {
      const response = await Request.GET('/deploy/soft_package')
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.tableData = data.data
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    get_soft_package_ids () {
      var softwareConfids = []
      this.$refs.tableData_ref.selection.map((item) => {
        softwareConfids.push(item.software_conf_id)
      })
      return softwareConfids
    },
    async software_package_del () {
      var softwarePackageInfo = this.$refs.tableData_ref.selection
      if (!softwarePackageInfo.length) {
        this.$message.error('请勾选一个配置文件')
      }
      const response = await Request.DELETE('/deploy/soft_package', { software_package_info: softwarePackageInfo })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.del_software_package_dialog = false
          this.software_package_query()
        } else {
          this.$message.error(data.msg)
        }
      }
    }
  },
  data () {
    return {
      del_software_package_dialog: false,
      clientH: document.documentElement.clientHeight,
      table_top: this.clientH - 50,
      fileList: [],
      rules: {
        software_name: [
          { required: true, message: '请输入软件名称', trigger: 'blur' }
        ],
        software_versions: [
          { required: true, message: '请输入版本号', trigger: 'blur' }
        ],
        software_package_zip_type: [
          { required: true, message: '请选择压缩类型', trigger: 'blur' }
        ],
        package_storage_type: [
          { required: true, message: '请选择存储类似', trigger: 'blur' }
        ]
      },
      software_package_form: {
        software_name: '',
        software_versions: '',
        software_package_zip_type: '',
        package_storage_type: ''
      },
      software_install_type_value: '',
      package_storage_type: [],
      software_package_zip_type_value: '',
      software_package_zip_type: [],
      adddialog: false,
      tableData: []
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
