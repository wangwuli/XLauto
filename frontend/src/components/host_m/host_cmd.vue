<template>
  <el-row>
      <div style="width: 100%">
        <el-button type="primary" size="mini" @click="hosts_add_target">主机加入<i class="el-icon-circle-plus-outline el-icon--right"></i></el-button>
        <el-button type="primary" size="mini" @click="updatedialog = true">上传脚本<i class="el-icon-upload el-icon--right"></i></el-button>
      </div>
    <div style="float:left; height: 500px; width: 410px; margin-bottom: 10px">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-upload" style="font-size: 15px; color: #91ca8c"/>
          <span>已存脚本</span>
          <el-select @change="UpdateScriptQuery" v-model="execute_script_group_code_key" placeholder="组" size="mini"
                     class="select-box-card-head" filterable default-first-option>
            <el-option
              v-for="item in execute_script_group_list"
              :key="item.code_key"
              :label="item.code_name"
              :value="item.code_key">
            </el-option>
          </el-select>
          <el-select @change="UpdateScriptQuery" v-model="execute_script_type_code_key" placeholder="类型" size="mini"
                     class="select-box-card-head" filterable default-first-option>
            <el-option
              v-for="item in execute_script_type_list"
              :key="item.code_key"
              :label="item.code_name"
              :value="item.code_key">
            </el-option>
          </el-select>
        </div>
        <el-table
          :data="update_script_list"
          ref = "update_script_list_value"
          style="width: 100%; height: 200px"
          size="mini">
          <el-table-column
            type="selection"
            width="55">
          </el-table-column>
          <el-table-column
            prop="file_name"
            label="脚本名"
            show-overflow-tooltip>
          </el-table-column>
          <el-table-column
            prop="file_type"
            label="类型"
            show-overflow-tooltip>
          </el-table-column>
          <el-table-column
            prop="file_group"
            label="组"
            show-overflow-tooltip>
          </el-table-column>
          <el-table-column
            prop="comment"
            label="操作"
            show-overflow-tooltip>
            <template slot-scope="scope">
              <el-button
                size="mini"
                @click="ScriptEdit(scope.$index, scope.row)" icon="el-icon-edit" style="padding: 0px" circle></el-button>
              <el-button
                size="mini"
                type="danger"
                @click="RmScriptDialog(scope.$index, scope.row)"  icon="el-icon-delete" style="padding: 0px" circle></el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-card>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-video-camera" style="font-size: 15px; color: #7289ab"/>
          <span>历史记录</span>
          <el-input v-model="search_history_value" placeholder="搜索" size="mini" style="width: 150px; float: right; margin-top: -5px "></el-input>
        </div>
        <el-table
          :data="history_script_list"
          style="width: 100%; height: 200px"
          ref="history_script_list_value"
          size="mini">
          <el-table-column
            type="selection"
            width="55">
          </el-table-column>
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
          <i class="el-icon-edit-outline" style="font-size: 15px; color: #eedd78"></i>
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
          <el-button @click="BindScript" type="primary" style="padding: 5px 20px;margin-top: -4px; margin-right: 5px; float: right">绑定</el-button>
          <el-button type="warning" style="padding: 5px 5px;margin-top: -4px; margin-right: 50px; float: right">执行</el-button>
        </div>
        <el-table
          :data="hosts_table_data"
          style="width: 100%; height: 455px"
          ref = "host_multiple_table_value"
          size="mini">
          <el-table-column
            type="selection"
            width="55">
          </el-table-column>
          <el-table-column
            prop="host_name"
            label="主机名"
            show-overflow-tooltip>
          </el-table-column>
          <el-table-column
            prop="host_ip"
            label="主机IP"
            show-overflow-tooltip>
          </el-table-column>
          <el-table-column
            label="执行动作"
            show-overflow-tooltip>
            <template slot-scope='if_host_execution_icon'>
              <el-tooltip v-if="if_host_execution_icon.row.existing_script_total" class="item" effect="dark" :content="if_host_execution_icon.row.existing_script_content_str" placement="top-start">
                <i class="el-icon-upload" style="font-size: 15px; color: #eedd78"/>
              </el-tooltip>
              <el-tooltip v-if="if_host_execution_icon.row.history_script_total" class="item" effect="dark" :content="if_host_execution_icon.row.history_script_content_str" placement="top-start">
                <i class="el-icon-video-camera" style="font-size: 15px; color: #7289ab"/>
              </el-tooltip>
              <el-tooltip  v-if="if_host_execution_icon.row.temporary_script_total" class="item" effect="dark" :content="if_host_execution_icon.row.temporary_script_content_str" placement="top-start">
                <i class="el-icon-edit-outline" style="font-size: 15px; color: #91ca8c"/>
              </el-tooltip>
           </template>
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
                @click="HostDelete(scope.$index, scope.row)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-card>
    </div>

    <el-dialog title="脚本上传" :visible.sync="updatedialog" class="update-dialog" width="500px" >
      <el-upload
        style="height: 200px"
        class="upload-demo"
        ref="upload"
        action="/hosts/update_script_file"
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

    <el-dialog
      title="提示"
      :visible.sync="if_dialog_rm_script"
      width="20%">
      <span>确认删除脚本</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="if_dialog_rm_script = false" size="mini">取 消</el-button>
        <el-button type="primary" @click="RmScript" size="mini">确 定</el-button>
      </span>
    </el-dialog>

    <el-dialog
      title="设置"
      :visible.sync="if_dialog_edit_script"
      width="300px">
        <el-select v-model="edit_script_group_code_key" placeholder="组" size="mini" style="width: 100px">
          <el-option
            v-for="item in execute_script_group_list"
            :key="item.code_key"
            :label="item.code_name"
            :value="item.code_key">
          </el-option>
        </el-select>
        <el-select v-model="edit_script_type_code_key" placeholder="类型" size="mini" style="width: 100px; padding-left: 20px">
          <el-option
            v-for="item in execute_script_type_list"
            :key="item.code_key"
            :label="item.code_name"
            :value="item.code_key">
          </el-option>
          </el-select>
      <span slot="footer" class="dialog-footer">
        <el-button @click="if_dialog_edit_script = false" size="mini">取 消</el-button>
        <el-button type="primary" @click="EditScript" size="mini">确 定</el-button>
      </span>
    </el-dialog>
  </el-row>
</template>
<script>
import * as Request from '@/general/request.js'
import { mapState } from 'vuex'

export default {
  data () {
    return {
      // page_height: document.documentElement.clientHeight - 150,
      // page_width: document.documentElement.clientWidth - 220,
      history_script_list: [],
      search_history_value: '',
      hosts_table_data: [],
      edit_script_group_code_key: '',
      edit_script_type_code_key: '',
      if_dialog_edit_script: false,
      edit_script_index: '',
      edit_script_row: '',
      if_dialog_rm_script: false,
      execute_script_group_list: [],
      execute_script_type_list: [],
      execute_script_group_code_key: '',
      execute_script_type_code_key: '',
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
      }],
      update_script_list: [],
      del_script_index: '',
      del_script_row: ''
    }
  },
  computed: {
    ...mapState({
      table_click_value: 'hosts_table_click_values'
    })
  },
  methods: {
    created_tabs_switch () {
      this.UpdateScriptQuery()
      this.ScriptGroupQuery()
      this.ScriptTypeQuery()
    },
    exceed_updte () {
      this.$message.warning('最多只能上传3个脚本')
    },
    submitUpload () {
      this.$refs.upload.submit()
      this.UpdateScriptQuery()
    },
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePreview (file) {
      console.log(file)
    },
    async UpdateScriptQuery () {
      const response = await Request.GET('/hosts/update_script_query', {
        file_type: this.execute_script_type_code_key,
        file_group: this.execute_script_group_code_key
      })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.update_script_list = data.data
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    async ScriptGroupQuery () {
      const response = await Request.GET('/general/code_query', { code_type: 'execute_script_group' })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.execute_script_group_list = data.data
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    async ScriptTypeQuery () {
      const response = await Request.GET('/general/code_query', { code_type: 'execute_script_type' })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.execute_script_type_list = data.data
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    RmScriptDialog (index, row) {
      this.if_dialog_rm_script = true
      this.del_script_index = index
      this.del_script_row = row
    },
    async RmScript () {
      const response = await Request.DELETE('/hosts/rm_script', { id: this.del_script_row.id })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.$message.success(data.msg)
          this.update_script_list.splice(this.del_script_index, 1)
          this.if_dialog_rm_script = false
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    ScriptEdit (index, row) {
      this.if_dialog_edit_script = true
      this.edit_script_index = index
      this.edit_script_row = row
    },
    async EditScript () {
      const response = await Request.POST('/hosts/edit_script', {
        id: this.edit_script_row.id,
        file_group: this.edit_script_group_code_key,
        file_type: this.edit_script_type_code_key
      })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.$message.success(data.msg)
          this.if_dialog_edit_script = false
          this.UpdateScriptQuery()
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    HostDelete (index, row) {
      this.hosts_table_data.splice(index, 1)
    },
    hosts_add_target () {
      if (this.table_click_value) {
        this.hosts_table_data = JSON.parse(JSON.stringify(this.table_click_value))
      } else {
        this.$message.warning('标靶中无选中服务器')
      }
    },
    ExistingScriptProcess (addDict) {
      var existingScriptContentList = []
      for (let ai = 0; ai < this.$refs.update_script_list_value.selection.length; ai++) {
        existingScriptContentList.push(this.$refs.update_script_list_value.selection[ai].file_name)
      }
      addDict = Object.assign(addDict, {
        existing_script_content_str: existingScriptContentList.join('\n'),
        existing_script_total: this.$refs.update_script_list_value.selection
      })
      return addDict
    },
    HistoryScriptProcess (addDict) {
      var historyScriptContentList = []
      for (let hi = 0; hi < this.$refs.history_script_list_value.selection.length; hi++) {
        historyScriptContentList.push(this.$refs.history_script_list_value.selection[hi].file_name)
      }
      addDict = Object.assign(addDict, {
        history_script_content_str: historyScriptContentList.join('\n'),
        history_script_total: this.$refs.history_script_list_value.selection
      })
      return addDict
    },
    TemporaryScriptProcess (addDict) {
      addDict = Object.assign(addDict, {
        temporary_script_content_str: '临时指令',
        temporary_script_total: this.temporary_script_text
      })
      return addDict
    },
    BindScript () {
      var HostMultipleTableSelection = this.$refs.host_multiple_table_value.selection
      if (HostMultipleTableSelection.length === 0) {
        this.$message.warning('请选择绑定主机')
        return false
      }
      var addDict = {}
      if (this.target_options_value === 'existing_script') {
        addDict = this.ExistingScriptProcess(addDict)
      } else if (this.target_options_value === 'history_script') {
        addDict = this.HistoryScriptProcess(addDict)
      } else if (this.target_options_value === 'temporary_script') {
        addDict = this.TemporaryScriptProcess(addDict)
      } else {
        addDict = this.ExistingScriptProcess(addDict)
        addDict = this.HistoryScriptProcess(addDict)
        addDict = this.TemporaryScriptProcess(addDict)
      }
      for (let hi = 0; hi < this.hosts_table_data.length; hi++) {
        for (let si = 0; si < HostMultipleTableSelection.length; si++) {
          if (this.hosts_table_data[hi].host_id === HostMultipleTableSelection[si].host_id) {
            this.$set(this.hosts_table_data, hi, Object.assign(this.hosts_table_data[hi], addDict))
          }
        }
      }
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
  .el-select-dropdown__item {
    font-size: 1px
  }
</style>
