<template>
  <div class="login-container">
    <div class="login-win">
      <div class="login-body">
        <div class="login-title">
          PMS项目管理系统
        </div>
        <div class="login-form">
          <el-form ref="loginFormRef" :model="loginForm" :rules="rules">
            <el-form-item prop="username" style="margin-bottom: 30px"> <!-- 用户名 -->
              <el-input v-model="loginForm.username" placeholder="用户名" prefix-icon="User"></el-input>
            </el-form-item>
            <el-form-item prop="password"> <!-- 密码 -->
              <el-input v-model="loginForm.password" placeholder="密码" prefix-icon="Lock"></el-input>
            </el-form-item>
            <el-form-item> <!-- 按钮 -->
              <el-button style="margin-top: 0px;width: 100%;" type="primary" @click="submitLoginForm">登录</el-button>
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
    //操作记录
    operationHistory() {
      const username = sessionStorage.getItem("username")
      const formData = new FormData();
      formData.append('user', username);
      formData.append('content', "登陆了页面");
      formData.append('operation_type', "用户管理");
      axios.post('/history/record_user_operation', formData, {
        headers: {
          'Content-Type': 'multipart/form-data' // 设置请求的 Content-Type
        }
      })
    },
    submitLoginForm() {
      this.$refs.loginFormRef.validate().then(async valid => {
        if (!valid) return;
        //true执行登录
        axios.post('/user/login/', {
          username: this.loginForm.username,
          password: this.loginForm.password,
        }, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
            .then((res) => {
              if (res.data.code !== 0) return ElMessage.error("登录失败！")
              ElMessage.success("登录成功")
              const userInfo = {
                username: this.loginForm.username,
              }
              const userInfoString = JSON.stringify(userInfo)
              const expiresDate = new Date();
              expiresDate.setFullYear(expiresDate.getFullYear() + 1); // 设置Cookie有效期为1年
              document.cookie = `userInfo=${encodeURIComponent(
                  userInfoString
              )}; expires=${expiresDate.toUTCString()}; path=/`;
              sessionStorage.setItem("username", this.loginForm.username)
              //存储token
              let token = res.data.token;
              window.sessionStorage.setItem("token", token)
              this.$router.push('/home')
              this.operationHistory()
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
