<template>
<el-dialog title="收货地址" :visible.sync="visible" :before-close="modalClose">
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
