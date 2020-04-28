<template>
  <el-drawer
  title="target!!!"
  :visible.sync="drawer"
  :direction="direction"
  :before-close="handleClose"
  :style="{width: clientW + 'px'}">
    <el-row>
    <el-button icon="el-icon-d-arrow-right" circle style="float:right" @click="littleRight"></el-button>
    <el-button icon="el-icon-d-arrow-left" circle style="float:left" @click="littleLeft"></el-button>
    </el-row>
    <el-form ref="hostFilterform" :model="host_filter_form" label-width="80px" size="mini" style="padding-left: 15px;padding-top: 15px"
             :inline="true">
      <el-form-item size="mini" label="选择项目">
        <el-select v-model="host_filter_form.host_project" placeholder="请选择" size="mini" style="width:130px">
          <el-option
            v-for="item in projectslist"
            :key="item.project_id"
            :label="item.project_name"
            :value="item.project_id">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item size="mini" label="选择类型">
        <el-select v-model="host_filter_form.host_type" placeholder="请选择" size="mini" style="width:130px">
          <el-option
            v-for="item in hosttypelist"
            :key="item.code_key"
            :label="item.code_name"
            :value="item.code_key">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item size="mini" label="主机IP">
        <el-input v-model="host_filter_form.host_ip" placeholder="请选择" style="width:130px"></el-input>
        <el-button icon="el-icon-search" circle style="margin-left:30px;" @click="getnewHostsinfo"></el-button>
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
</template>

<script>
import * as Request from '@/general/request.js'

export default {
  name: 'hostlist',
  data () {
    return {
      clientW: document.documentElement.clientWidth,
      host_filter_form: {
        host_project: '',
        host_type: '',
        host_ip: ''
      },
      drawer: false,
      direction: 'ltr',
      tableData: [],
      multipleSelection: [],
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
      this.$message.success('点击标记：' + row.host_ip + '  成功')
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
      this.multipleSelection = val
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
    }
  }
}
</script>

<style scoped>

</style>
