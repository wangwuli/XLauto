<template>
  <el-row>
    <el-button type="primary" size="mini">角色校验</el-button>
    <el-select v-model="value" placeholder="可选角色" size="mini" style="padding-left: 10px">
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>
    <el-button type="primary" size="mini">绑定</el-button>

    <el-select v-model="value" placeholder="角色" size="mini" style="padding-left: 10px">
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>
    <el-button type="primary" size="mini">过滤</el-button>

    <el-button type="primary" size="mini" @click="configuration_dialog = true">配置</el-button>
    <el-button type="danger" size="mini">卸载</el-button>
    <el-button type="warning" size="mini">部署</el-button>
    <el-table
      size="mini"
      ref="multipleTable"
      :data="tableData"
      tooltip-effect="dark"
      style="width: 100%"
      @selection-change="handleSelectionChange">
      <el-table-column
        type="selection"
        width="55">
      </el-table-column>
      <el-table-column
        label="IP"
        width="120">
        <template slot-scope="scope">{{ scope.row.date }}</template>
      </el-table-column>
      <el-table-column
        prop="name"
        label="项目"
        width="120">
      </el-table-column>
      <el-table-column
        prop="address"
        label="现有角色"
        show-overflow-tooltip>
      </el-table-column>
      <el-table-column
        prop="status"
        label="运行状态"
        show-overflow-tooltip>
      </el-table-column>
    </el-table>

    <el-dialog title="配置" :visible.sync="configuration_dialog">
      <div style="height: 60vh; overflow: auto">
        <el-tabs v-model="activeName" @tab-click="configurationHandleclick">
          <el-tab-pane label="通用配置" name="configuration_general">
            <el-form :model="configuration_form" size="mini" :inline="true">
              <el-form-item label="系统">
                <el-radio v-model="configuration_form.system" label="centos">CentOS8(RHEL8)</el-radio>
              </el-form-item>
              <el-row>
              <el-form-item label="防火墙">
                <el-switch
                  v-model="configuration_form.firewalld"
                  active-color="#13ce66"
                  inactive-color="#ff4949">
                </el-switch>
              </el-form-item>
              <el-form-item label="SELinux" style="margin-left: 5vh">
                <el-switch
                  v-model="configuration_form.selinux"
                  active-color="#13ce66"
                  inactive-color="#ff4949">
                </el-switch>
              </el-form-item>
              </el-row>
              <el-form-item label="仓库地址">
                <el-select v-model="configuration_form.repository" placeholder="请选择使用的仓库">
                  <el-option
                  v-for="item in kubernetes_repository_all_type"
                  :key="item.code_key"
                  :label="item.code_name"
                  :value="item.code_key">
                </el-option>
                </el-select>
              </el-form-item>
            </el-form>
          </el-tab-pane>
          <el-tab-pane label="Master配置" name="second">配置管理</el-tab-pane>
          <el-tab-pane label="Node配置" name="third">角色管理</el-tab-pane>
          <el-tab-pane label="其他" name="fourth">其他</el-tab-pane>
        </el-tabs>
      </div>
      <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false" size="mini">取 消</el-button>
          <el-button type="primary" @click="kubernetesInstallSubmit" size="mini">确 定</el-button>
      </div>
    </el-dialog>

  </el-row>
</template>

<script>
import * as Request from '@/general/request.js'

export default {
  name: 'soft_deploy',
  data () {
    return {
      kubernetes_repository_all_type: [],
      activeName: 'configuration_general',
      configuration_dialog: false,
      configuration_form: {
        repository: '',
        system: 'centos',
        firewalld: false,
        selinux: false
      },
      options: [{
        value: '选项1',
        label: '黄金糕'
      }, {
        value: '选项2',
        label: '双皮奶'
      }, {
        value: '选项3',
        label: '蚵仔煎'
      }, {
        value: '选项4',
        label: '龙须面'
      }, {
        value: '选项5',
        label: '北京烤鸭'
      }],
      tableData: [{
        date: '192.168.1.1',
        name: '本部',
        address: 'Master'
      }, {
        date: '192.168.1.2',
        name: '本部',
        address: 'Node'
      }, {
        date: '192.168.1.3',
        name: '本部',
        address: 'Node'
      }, {
        date: '192.168.1.4',
        name: '本部',
        address: 'Node'
      }, {
        date: '192.168.1.5',
        name: '本部',
        address: 'Node'
      }, {
        date: '192.168.1.6',
        name: '本部',
        address: 'Node'
      }, {
        date: '192.168.1.7',
        name: '本部',
        address: 'Node'
      }],
      multipleSelection: []
    }
  },
  created () {
    this.kubernetesRepositoryQuery()
  },
  methods: {
    handleSelectionChange (val) {
      this.multipleSelection = val
    },
    configurationHandleclick (tab, event) {
      console.log(tab, event)
    },
    async kubernetesRepositoryQuery () {
      const response = await Request.GET('/general/code_query', { code_type: 'kubernetes_repository_type' })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          // this.$message.success(data.msg)
          this.kubernetes_repository_all_type = data.data
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    async kubernetesInstallSubmit () {
      const response = await Request.POST('/deploy/kubernetes_install', this.configuration_form)
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.$message.success(data.msg)
        } else {
          this.$message.error(data.msg)
        }
      }
    }
  }
}
</script>

<style scoped>

</style>
