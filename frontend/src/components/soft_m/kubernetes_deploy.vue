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

    <el-button type="primary" size="mini">配置</el-button>
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
    </el-table>
  </el-row>
</template>

<script>
export default {
  name: 'soft_deploy',
  data () {
    return {
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
  methods: {
    handleSelectionChange (val) {
      this.multipleSelection = val
    }
  }
}
</script>

<style scoped>

</style>
