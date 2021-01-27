<template>
      <el-select v-model="code_key_value" placeholder="请选择" size="mini">
        <el-option
          v-for="item in sys_code_list"
          :key="item.code_key"
          :label="item.code_name"
          :value="item.code_key">
        </el-option>
      </el-select>
</template>

<script>
import * as Request from '@/general/request.js'
export default {
  name: 'select-sys-code',
  data () {
    return {
      sys_code_list: [],
      code_key_value: ''
    }
  },
  mounted () {
    this.get_sys_code()
  },
  model: {
    prop: 'return_value',
    event: 'change'
  },
  watch: {
    return_value (val) {
      this.code_key_value = val
    },
    code_key_value (val) {
      this.$emit('change', val)
    }
  },
  props: {
    code_type: {
      type: String,
      default: null
    }
  },
  methods: {
    async get_sys_code () {
      const response = await Request.GET('/general/code_query', { code_type: this.code_type })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          this.sys_code_list = data.data
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
