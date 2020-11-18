<template>
  <el-row>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>基本信息</span>
        <el-button style="float: right; padding: 3px 0" type="text">保存</el-button>
      </div>
      <div>
      <el-form :model="form" size="mini" ref="form_data" :rules="rules">
        <el-form-item label="API地址：" :label-width="formLabel_width" prop="portal_url">
          <el-input v-model="form.portal_url" autocomplete="off" size="mini" placeholder="请输入URL"
                     class="input_basic_information"></el-input>
        </el-form-item>

        <el-form-item label="用户名：" :label-width="formLabel_width" prop="portal_login_user">
          <el-input v-model="form.portal_login_user" autocomplete="off" size="mini" placeholder="请输入"
                     class="input_basic_information" ></el-input>
        </el-form-item>

        <el-form-item label="密码：" :label-width="formLabel_width" prop="portal_login_pwd">
          <el-input v-model="form.portal_login_pwd" autocomplete="off" size="mini" placeholder="请输入"
                    class="input_basic_information" show-password></el-input>
        </el-form-item>
      </el-form>
        </div>
    </el-card>
  </el-row>
</template>

<script>
export default {
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
</style>
