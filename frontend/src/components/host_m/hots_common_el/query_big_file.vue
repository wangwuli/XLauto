<template>
<el-dialog title="收货地址" :visible.sync="visible" :before-close="modalClose">
  <el-form :model="form">
    <el-form-item label="活动名称" :label-width="formLabelWidth">
      <el-input v-model="form.name" autocomplete="off"></el-input>
    </el-form-item>
    <el-form-item label="活动区域" :label-width="formLabelWidth">
      <el-select v-model="form.region" placeholder="请选择活动区域">
        <el-option label="区域一" value="shanghai"></el-option>
        <el-option label="区域二" value="beijing"></el-option>
      </el-select>
    </el-form-item>
  </el-form>
  <div slot="footer" class="dialog-footer">
    <el-button @click="dialogq_bigfile = false">取 消</el-button>
    <el-button type="primary" @click="dialogq_bigfile = false">确 定</el-button>
  </div>
</el-dialog>
</template>

<script>
export default {
  name: 'zabbix',
  data () {
    return {
      form: {
        name: '',
        region: ''
      }
    }
  },
  props: {
    visible: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    modalClose () {
      this.$emit('update:visible', false)
    }
  }
}
</script>

<style scoped>

</style>
