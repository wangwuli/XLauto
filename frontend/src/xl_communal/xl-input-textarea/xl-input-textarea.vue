<template>
  <el-input
    :rows="textarea_rows"
    type="textarea"
    placeholder="未显示内容"
    v-model="textarea">
  </el-input>
</template>

<script>

export default {
  name: 'xl-input-textarea',
  data () {
    return {
      textarea: '',
      textarea_rows: Math.floor((window.innerHeight - 80) / this.altitude)
    }
  },
  mounted () {
  },
  model: {
    prop: 'return_value',
    event: 'change'
  },
  watch: {
    return_value (val) {
      this.textarea = val
    },
    textarea (val) {
      this.$emit('change', val)
    }
  },
  props: {
    altitude: {
      type: Number,
      default: 30
    }
  },
  methods: {
  }
}
</script>

<style scoped>

</style>
