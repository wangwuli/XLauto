<template>
  <el-row>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>基本信息</span>
        <el-button style="float: right; padding: 3px 0" type="text" @click="ZabbixConfSave">保存</el-button>
      </div>
      <div>
      <el-form :model="form" size="mini" ref="form_data" :rules="rules">
        <el-row>
          <el-form-item label="启用：" :label-width="formLabel_width" prop="portal_url">
          <el-switch
            style="display: block"
            v-model="form.portal_disabled"
            active-color="#13ce66"
            inactive-color="#ff4949">
          </el-switch>
          </el-form-item>
        <el-form-item label="API地址：" :label-width="formLabel_width" prop="portal_url">
          <el-input v-model="form.portal_url" autocomplete="off" size="mini" placeholder="请输入URL"
                     class="input_url_basic_information"></el-input>
        </el-form-item>
        </el-row>
        <el-row>
        <el-form-item label="用户名：" :label-width="formLabel_width" prop="portal_login_user">
          <el-input v-model="form.portal_login_user" autocomplete="off" size="mini" placeholder="请输入"
                     class="input_basic_information" ></el-input>
        </el-form-item>

        <el-form-item label="密码：" :label-width="formLabel_width" prop="portal_login_pwd">
          <el-input v-model="form.portal_login_pwd" autocomplete="off" size="mini" placeholder="请输入"
                    class="input_basic_information" show-password></el-input>
        </el-form-item>
          </el-row>
      </el-form>
        </div>
    </el-card>
  </el-row>
</template>

<script>
import * as Request from '@/general/request.js'

export default {
  created () {
    this.ZabbixConfQuery()
  },
  name: 'zabbix',
  data () {
    return {
      form: {},
      formLabel_width: '200px',
      rules: { // 表单验证
        sys_code_type: [
          { required: true, message: '请输入类型', trigger: 'blur' },
          { min: 1, max: 50, message: '长度在 1 到 50个字符', trigger: 'blur' },
          {
            trigger: 'blur',
            validator: (rule, value, callback) => {
              this.get_type_name()
              callback()
            }
          }
        ]
      }
    }
  },
  methods: {
    async ZabbixConfQuery () {
      const response = await Request.GET('/setting/main', { portal_label: 'zabbix' })
      if (response && response.data) {
        var data = response.data
        if (data.success) {
          if (data.data.portal_disabled === 1) {
            data.data.portal_disabled = false
          } else {
            data.data.portal_disabled = true
          }
          this.form = data.data
        } else {
          this.$message.error(data.msg)
        }
      }
    },
    async ZabbixConfSave () {
      const response = await Request.POST('/setting/main/zabbix', { form: this.form })
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
.box-card {
    /*width: 480px;*/
  }
.input_basic_information {
  width: 200px;
}

.input_url_basic_information {
  width: 400px;
}
</style>
