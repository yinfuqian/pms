<template>
  <div class="login-container">
    <div class="login-win">
      <div class="login-body">
        <div class="login-title">
          PMS项目管理系统
        </div>
        <div class="login-form">
          <el-form :model="loginForm" :rules="rules" ref="loginFormRef">
            <el-form-item style="margin-bottom: 30px" prop="username"> <!-- 用户名 -->
              <el-input prefix-icon="User" placeholder="用户名" v-model="loginForm.username"></el-input>
            </el-form-item>
            <el-form-item prop="password"> <!-- 密码 -->
              <el-input prefix-icon="Lock" placeholder="密码" v-model="loginForm.password"></el-input>
            </el-form-item>
            <el-form-item> <!-- 按钮 -->
              <el-button type="primary" @click="submitLoginForm" style="margin-top: 0px;width: 100%;">登录</el-button>
            </el-form-item>
          </el-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {User} from "@element-plus/icons-vue";
import axios from "axios";
import {defineComponent} from "vue";
import {ElMessage} from "element-plus";
export default {
  name: "PmsUserLogin",
  components: {User},
  data() {
    return {
      loginForm: {
        username: '',
        password: '',
      },
      /* 验证用户名密码是否合法*/
      rules: {
        username: [
          {required: true, message: "账号不能为空", trigger: 'blur'},
          {min: 3, max: 10, message: "长度在3到10个字符", trigger: 'blur'}],
        password: [
          {required: true, message: "密码不能为空", trigger: 'blur'},
          {min: 6, max: 15, message: '长度在 6 到 15 个字符', trigger: 'blur'}]
      },
    };
  },/* 登录*/
  methods: {
    submitLoginForm() {
      this.$refs.loginFormRef.validate().then(async valid => {
        if (!valid) return;
        //true执行登录
        axios.post('/login/', {
          username:this.loginForm.username,
          password:this.loginForm.password,
        })
            .then((res) => {
              console.log(res.data);
              if(res.data.code !== 0) return ElMessage.error("登录失败！")
              ElMessage.success("登录成功")
              //存储token
              let token =res.data.token;
              //console.log("登录成功，token为：",token)
              window.sessionStorage.setItem("token",res.data.token)
              this.$router.push('/home')
            })
      });
    }
  }
}
</script>
<style scoped>
.login-container {
  background-image: url('../static/bj.png');
  background-size: cover;
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
  right: 0;
}

.login-win {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 400px;
  height: 300px;
  padding: 25px 25px;
  border-radius: 5px;
  background-color: lavenderblush;

}

.login-body {
  width: 100%;
}

.login-title {
  text-align: center;
  font-size: 20px;
  font-weight: bold;
  color: cornflowerblue;
  margin-bottom: 45px;
  margin-top: 15px;
}


yuan {
  position: absolute;
  bottom: 30px;
  /*靠下 width: 100 %;*/
  padding: 0 20px;
  /*上下内边距0，左右内边距20px*/
  /*border-box为元素指定的任何内边距和边框都将在已设定的宽度和高度内进行绘制。
  实际宽度会是width减去border + padding的计算值
  此处是为了不让input超出我们的登录父div*/
  box-sizing: border-box;
}
</style>
