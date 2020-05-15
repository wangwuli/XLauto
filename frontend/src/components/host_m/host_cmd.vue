<template>
  <el-row>
      <div style="width: 100%">
        <el-button type="primary" size="mini" @click="updatedialog = true">主机加入<i class="el-icon-circle-plus-outline el-icon--right"></i></el-button>
        <el-button type="primary" size="mini" @click="updatedialog = true">上传脚本<i class="el-icon-upload el-icon--right"></i></el-button>
      </div>
    <div style="float:left; height: 500px; width: 410px; margin-bottom: 10px">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>已存脚本</span>
          <el-select v-model="value" placeholder="类型" size="mini" class="select-box-card-head">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
          <el-select v-model="value" placeholder="组" size="mini" class="select-box-card-head">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </div>
        <el-table
          :data="tableData"
          style="width: 100%; height: 200px"
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
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>历史记录</span>
          <el-input v-model="input" placeholder="搜索" size="mini" style="width: 150px; float: right; margin-top: -5px "></el-input>
        </div>
        <el-table
          :data="tableData"
          style="width: 100%; height: 200px"
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
            label="最后执行时间"
            show-overflow-tooltip>
          </el-table-column>
        </el-table>
      </el-card>
    </div>
    <div style="float:left; height: 500px; width: 410px; margin-bottom: 10px">
      <el-card class="box-card-temporary-text">
        <div slot="header" class="clearfix">
          <span>临时指令内容</span>
        </div>
        <el-input
          type="textarea"
          :rows="21"
          placeholder="请输入内容"
          v-model="temporary_script_text">
        </el-input>
      </el-card>
    </div>
    <div style="float:left; height: 600px; width: 820px">
      <el-card class="box-card-host-basket">
        <div slot="header" class="clearfix" style="height: 16px">
          <span>执行目标</span>
          <el-select v-model="target_options_value" placeholder="绑定目标" size="mini" class="select-box-card-head" style="width: 150px">
            <el-option
              v-for="item in target_options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
          <el-button type="primary" style="padding: 5px 5px;margin-top: -4px; margin-right: 5px; float: right">绑定</el-button>
        </div>
        <el-table
          :data="tableData"
          style="width: 100%; height: 455px"
          size="mini">
          <el-table-column
            prop="date"
            label="主机名"
            show-overflow-tooltip>
          </el-table-column>
          <el-table-column
            prop="name"
            label="执行动作"
            show-overflow-tooltip>
          </el-table-column>
          <el-table-column
            prop="address"
            label="结果"
            show-overflow-tooltip>
          </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button
                size="mini"
                @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
              <el-button
                size="mini"
                type="danger"
                @click="handleDelete(scope.$index, scope.row)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-card>
    </div>

    <el-dialog title="脚本上传" :visible.sync="updatedialog" class="update-dialog" width="500px" >
      <el-upload
        style="height: 200px"
        class="upload-demo"
        ref="uplo--color-primaryad"
        action="/host_cmd/update_file"
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
      // page_height: document.documentElement.clientHeight - 150,
      // page_width: document.documentElement.clientWidth - 220,
      target_options_value: '',
      temporary_script_text: '',
      updatedialog: false,
      fileList: [
      ],
      target_options: [{
        value: 'all',
        label: '所有选择'
      }, {
        value: 'existing_script',
        label: '已存脚本'
      }, {
        value: 'history_script',
        label: '历史记录'
      }, {
        value: 'temporary_script',
        label: '临时指令'
      }]
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
    width: 405px;
    height: 226px;
    font-size: 5px;
    margin : 5px 5px 5px 5px;
    padding-bottom: 20px;
  }
  .update-dialog .el-dialog__body {
    /*width: 50px;*/
  }
   .el-card /deep/ .el-card__header {
    padding: 10px 20px;
  }

  .el-card /deep/ .el-card__body {
    padding: 0px;
  }
  .box-card-host-basket {
    width: 815px;
    height: 500px;
    font-size: 5px;
    margin : 5px 5px 5px 5px;
  }

  .box-card-temporary-text {
    width: 405px;
    height: 100%;
    font-size: 5px;
    margin : 5px 5px 5px 5px;
  }
  .select-box-card-head {
    float: right;
    width: 100px;
    margin-top: -5px;
    margin-right: 0px
  }
</style>
