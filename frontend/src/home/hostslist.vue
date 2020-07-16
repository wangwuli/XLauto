<template>
  <el-row>
    <el-drawer
    title="target!!!"
    :visible.sync="drawer"
    :direction="direction"
    :before-close="handleClose"
    :style="{width: clientW + 'px'}">
      <div>
        <el-drawer
          title="新增主机"
          :direction="direction"
          :append-to-body="true"
          :before-close="handleClose"
          :visible.sync="add_host_drawer"
          :style="{width: clientW/1.5 + 'px',height: clientH/2 + 'px',marginTop: clientH/10 + 'px'}">
          <el-form ref="hostFilterform" style="padding-left: 15px;">
            <el-form-item size="mini" label="IPs" style="padding-left: 35px;">
            <el-input v-model="host_add_form.hosts_input_text" size="mini" placeholder="IP支持.1-254与1，2..输入" class="add_input_style"></el-input>
            </el-form-item>
            <el-form-item size="mini" label="用户名" style="padding-left: 13px;">
            <el-input v-model="host_add_form.user_name" size="mini" placeholder="请输入" class="add_input_style"></el-input>
            </el-form-item>
            <el-form-item size="mini" label="密码" style="padding-left: 28px;">
            <el-input v-model="host_add_form.password" size="mini" placeholder="请输入" class="add_input_style" show-password></el-input>
            </el-form-item>
            <el-form-item size="mini" label="选择项目">
              <el-select v-model="host_add_form.host_project" placeholder="请选择" size="mini" class="add_input_style">
                <el-option
                  v-for="item in projectslist"
                  :key="item.project_id"
                  :label="item.project_name"
                  :value="item.project_id">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item size="mini" label="选择类型">
              <el-select v-model="host_add_form.host_type" placeholder="请选择" size="mini" class="add_input_style">
                <el-option
                  v-for="item in hosttypelist"
                  :key="item.code_key"
                  :label="item.code_name"
                  :value="item.code_key">
                </el-option>
              </el-select>
            </el-form-item>
          </el-form>
          <el-button type="primary" size="mini" icon="el-icon-finished" circle style="margin-right:30px;float: right" @click="addhost_dialog_visible = true"></el-button>
        </el-drawer>
      </div>
      <el-row>
      <el-button icon="el-icon-d-arrow-right" circle style="float:right" @click="littleRight"></el-button>
      <el-button icon="el-icon-d-arrow-left" circle style="float:left" @click="littleLeft"></el-button>
      </el-row>
      <el-form ref="hostFilterform" :model="host_filter_form" label-width="80px" size="mini" style="padding-left: 15px;padding-top: 15px"
               :inline="true">
        <el-form-item size="mini" label="选择项目">
          <el-select v-model="host_filter_form.host_project" placeholder="请选择" size="mini" class="select_input_style">
            <el-option
              v-for="item in projectslist"
              :key="item.project_id"
              :label="item.project_name"
              :value="item.project_id">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item size="mini" label="选择类型">
          <el-select v-model="host_filter_form.host_type" placeholder="请选择" size="mini" class="select_input_style">
            <el-option
              v-for="item in hosttypelist"
              :key="item.code_key"
              :label="item.code_name"
              :value="item.code_key">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item size="mini" label="主机IP">
          <el-input v-model="host_filter_form.host_ip" placeholder="请选择" class="select_input_style"></el-input>
          <el-button icon="el-icon-search" circle style="margin-left:30px;" @click="getnewHostsinfo"></el-button>
          <el-button icon="el-icon-circle-plus-outline" circle style="margin-left:30px;" @click="add_host_drawer = true" type="primary"></el-button>
        </el-form-item>
      </el-form>
    <el-table
      @row-click="hoststableClick"
      size="mini"
      ref="multipleTable"
      :data="tableData"
      tooltip-effect="dark"
      style="width: 100%; height:50%"
      @selection-change="handleSelectionChange">
      <el-table-column
        type="selection"
        width="55">
      </el-table-column>
      <el-table-column
        prop="host_ip"
        label="IP"
        :fit="true"
        show-overflow-tooltip>
      </el-table-column>
      <el-table-column
        prop="host_type_text"
        label="主机类"
        :fit="true"
        show-overflow-tooltip>
      </el-table-column>
      <el-table-column
        prop="host_name"
        label="主机名"
        :fit="true"
        show-overflow-tooltip>
      </el-table-column>
    </el-table>
    <el-pagination
      size="mini"
      :pager-count=5
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :page-sizes="host_page_sizes"
      :page-size="host_date_size"
      :current-page="host_date_page"
      layout="total, sizes, pager"
      :small="true"
      style="text-align: center"
      :total="host_date_total">
    </el-pagination>
    </el-drawer>
    <el-dialog
      :modal-append-to-body='false'
      title="提示"
      :visible.sync="addhost_dialog_visible"
      width="20%">
      <span>提交创建主机</span>
      <span slot="footer" class="dialog-footer">
      <el-button @click="addhost_dialog_visible = false" size="mini">取 消</el-button>
      <el-button type="primary" @click="addHostrequest" size="mini">确 定</el-button>
      </span>
    </el-dialog>
  </el-row>
</template>

<script>
import * as Request from '@/general/request.js'

export default {
  name: 'hostlist',
  data () {
    return {
      addhost_dialog_visible: false,
      hosts_input_text: '',
      add_host_drawer: false,
      clientW: document.documentElement.clientWidth,
      clientH: document.documentElement.clientHeight,
      host_filter_form: {
        host_project: '',
        host_type: '',
        host_ip: ''
      },
      host_add_form: {
        host_project: '',
        host_type: '',
        hosts_input_text: '',
        user_name: '',
        user_pass: ''
      },
      drawer: false,
      direction: 'ltr',
      tableData: [],
      value: '',
      hosttypelist: [],
      projectslist: [],
      host_date_size: 20,
      host_date_page: 1,
      host_date_total: 0,
      host_page_sizes: [10, 20, 50, 100]
    }
  },
  created () {
    this.hostslistQuery()
    this.hosttypeQuery()
    this.projectsQuery()
  },
  methods: {
    hoststableClick (row) {
      this.edittableClickValue = row
      this.$message.success('点击标记：' + row.host_ip + '  成功，正在载入，请稍后')
    },
    handleSizeChange (val) {
      this.host_date_size = val
      this.hostslistQuery()
    },
    handleCurrentChange (val) {
      this.host_date_page = val
      this.hostslistQuery()
    },
    getnewHostsinfo () {
      this.hostslistQuery()
    },
    littleLeft () {
      this.clientW -= this.clientW * 0.2
    },
    littleRight () {
      this.clientW += this.clientW * 0.2
    },
    open_close (value) {
      this.drawer = value
    },
    handleClose (done) {
      done()
    },
    toggleSelection (rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row)
        })
      } else {
        this.$refs.multipleTable.clearSelection()
      }
    },
    handleSelectionChange (val) {
      // this.multipleSelection = val
      this.HostTableClickValues = val
    },
    async addHostrequest () {
      const response = await Request.POST('/hosts/add_host', this.host_add_form)
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.$message.success(data.msg)
          this.addhost_dialog_visible = false
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    async hostslistQuery () {
      var datas = JSON.parse(JSON.stringify(this.host_filter_form))
      datas.size = this.host_date_size
      datas.page = this.host_date_page
      const response = await Request.GET('/home/hosts_query', datas)
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.$message.success(data.msg)
          this.tableData = data.data
          this.host_date_total = data.count
          if (this.host_date_total > 100) {
            this.host_page_sizes = [
              parseInt(this.host_date_total / 10),
              parseInt(this.host_date_total / 5),
              parseInt(this.host_date_total / 2),
              parseInt(this.host_date_total)
            ]
          }
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    async hosttypeQuery () {
      const response = await Request.GET('/general/code_query', { code_type: 'host_type' })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          // this.$message.success(data.msg)
          this.hosttypelist = data.data
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    async projectsQuery () {
      const response = await Request.GET('/home/projects')
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          // this.$message.success(data.msg)
          this.projectslist = data.data
        } else {
          this.$message.error(data.msg)
        }
      }
    }
  },
  computed: {
    // ...mapState({
    //   table_click_value: 'host_table_click_value'
    // }),
    edittableClickValue: {
      get () {
        return this.$store.state.host_table_click_value
      },
      set (val) {
        this.$store.state.host_table_click_value = val
      }
    },
    HostTableClickValues: {
      get () {
        return this.$store.state.hosts_table_click_values
      },
      set (val) {
        this.$store.state.hosts_table_click_values = val
      }
    }
  }
}
</script>

<style scoped>

  .select_input_style{
    width: 130px;
  }
  .add_input_style{
    width: 180px;
  }

</style>
