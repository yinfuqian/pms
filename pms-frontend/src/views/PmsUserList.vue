<template>
  <div>
    <!-- 面包屑导航 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="'/home'">首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="'/users'">用户管理</el-breadcrumb-item>
      <el-breadcrumb-item>用户列表</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card>
      <!-- 搜索与添加区域 -->
      <div class="search-area">
        <el-row :gutter="20">
          <!--        指定每个栏位为20-->
          <el-col :span="20">
            <el-input v-model='queryInfo.query' clearable placeholder="请输入用户名" @clear="getUserList">
              <template #append>
                <el-button slot="append" @click="getUserList">
                  <el-icon>
                    <Search/>
                  </el-icon>
                </el-button>
              </template>
            </el-input>
          </el-col>
          <el-col :span="4">
            <el-button type="primary" @click="openAddDialog">添加用户</el-button>
          </el-col>
        </el-row>
      </div>
      <!--      用户列表区域-->
      <el-table :data="userlist" border stripe>
        <el-table-column type="index"></el-table-column>
        <el-table-column label="姓名" prop="username"></el-table-column>
        <el-table-column label="昵称" prop="usernicname"></el-table-column>
        <el-table-column label="岗位" prop="userjob"></el-table-column>
        <el-table-column label="地区" prop="userbase"></el-table-column>
        <el-table-column label="工号" prop="userworknum"></el-table-column>
        <el-table-column label="邮箱" prop="useremail"></el-table-column>
        <el-table-column label="电话" prop="userphonenum"></el-table-column>
        <el-table-column label="操作" width="180px">
          <template v-slot="scope">
            <!-- 修改按钮 -->
            <el-button type="primary" @click="showEditDialog(scope.row.username)">
              <el-icon>
                <edit/>
              </el-icon>
            </el-button>
            <!-- 删除按钮 -->
            <el-button type="danger" @click="showDeleteDialog(scope.row.id)">
              <el-icon>
                <delete/>
              </el-icon>
            </el-button>
          </template>
        </el-table-column>
      </el-table>
      <!--        分页功能-->
      <el-config-provider :locale="zhCn">
        <el-pagination
            :current-page="queryInfo.pageNum"
            :page-size="queryInfo.pageSize"
            :page-sizes="[1, 2, 5, 10]"
            :total="count"
            layout="total, sizes, prev, pager, next, jumper"
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
        />
      </el-config-provider>
    </el-card>
    <!-- 添加用户弹窗 -->
    <el-dialog v-model="addDialogVisible" title="添加用户" width="50%">
      <!-- 内容主体区 -->
      <el-form ref="addUserFormRef" :model="addUserForm" :rules="addUserFormRules" label-width="70px">
        <el-form-item label="用户名" prop="username"> <!-- prop是验证规则属性 -->
          <el-input v-model="addUserForm.username"></el-input>
        </el-form-item>
        <el-form-item label="昵称" prop="usernicname"> <!-- prop是验证规则属性 -->
          <el-input v-model="addUserForm.usernicname"></el-input>
        </el-form-item>
        <el-form-item label="岗位" prop="userjob"> <!-- prop是验证规则属性 -->
          <el-select v-model="addUserForm.userjob" placeholder="点击选择">
            <el-option label="PM" value="PM"/>
            <el-option label="TM" value="TM"/>
            <el-option label="合作企业员工" value="OutTM"/>
            <el-option label="管理员" value="Admin"/>
          </el-select>
        </el-form-item>
        <el-form-item label="地区" prop="userbase">
          <el-select v-model="addUserForm.userbase" placeholder="点击选择">
            <el-option label="北京" value="BJ"/>
            <el-option label="上海" value="SH"/>
            <el-option label="天津" value="TJ"/>
            <el-option label="重庆" value="CQ"/>
            <el-option label="河北" value="HE"/>
            <el-option label="山西" value="SX"/>
            <el-option label="辽宁" value="LN"/>
            <el-option label="吉林" value="JL"/>
            <el-option label="黑龙江" value="HL"/>
            <el-option label="江苏" value="JS"/>
            <el-option label="浙江" value="ZJ"/>
            <el-option label="安徽" value="AH"/>
            <el-option label="福建" value="FJ"/>
            <el-option label="江西" value="JX"/>
            <el-option label="山东" value="SD"/>
            <el-option label="河南" value="HA"/>
            <el-option label="湖北" value="HB"/>
            <el-option label="湖南" value="HN"/>
            <el-option label="广东" value="GD"/>
            <el-option label="广西" value="GX"/>
            <el-option label="海南" value="HI"/>
            <el-option label="四川" value="SC"/>
            <el-option label="贵州" value="GZ"/>
            <el-option label="云南" value="YN"/>
            <el-option label="西藏" value="XZ"/>
            <el-option label="陕西" value="SN"/>
            <el-option label="甘肃" value="GS"/>
            <el-option label="青海" value="QH"/>
            <el-option label="宁夏" value="NX"/>
            <el-option label="新疆" value="XJ"/>
            <el-option label="台湾" value="TW"/>
            <el-option label="香港" value="HK"/>
            <el-option label="澳门" value="MO"/>
          </el-select>
          <!--          <el-input v-model="addUserForm.userbase"></el-input>-->
        </el-form-item>
        <el-form-item label="工号" prop="userworknum"> <!-- prop是验证规则属性 -->
          <el-input v-model="addUserForm.userworknum"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="addUserForm.password" type="password"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="useremail">
          <el-input v-model="addUserForm.useremail"></el-input>
        </el-form-item>
        <el-form-item label="手机" prop="userphonenum">
          <el-input v-model="addUserForm.userphonenum"></el-input>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer" class="dialog-footer">
      <el-button @click="addDialogVisible = false">取 消</el-button>
      <el-button type="primary" @click="createUser">确 定</el-button></span>
      <!--      修改用户弹窗-->
    </el-dialog>
    <!--    修改用户弹窗-->
    <el-dialog v-model="editDialogVisible" title="修改用户" width="50%">
      <!-- 内容主体区 -->
      <el-form ref="editUserFormRef" :model="editUserForm" :rules="addUserFormRules" label-width="70px">
        <el-form-item label="用户名" prop="username"> <!-- prop是验证规则属性 -->
          <el-input v-model="editUserForm.username" disabled></el-input>
        </el-form-item>
        <el-form-item label="昵称" prop="usernicname"> <!-- prop是验证规则属性 -->
          <el-input v-model="editUserForm.usernicname"></el-input>
        </el-form-item>
        <el-form-item label="岗位" prop="userjob"> <!-- prop是验证规则属性 -->
          <el-select v-model="editUserForm.userjob" placeholder="点击选择">
            <el-option label="PM" value="PM"/>
            <el-option label="TM" value="TM"/>
            <el-option label="合作企业员工" value="OutTM"/>
            <el-option label="管理员" value="Admin"/>
          </el-select>
        </el-form-item>
        <el-form-item label="地区" prop="userbase">
          <el-select v-model="editUserForm.userbase" placeholder="点击选择">
            <el-option label="北京" value="BJ"/>
            <el-option label="上海" value="SH"/>
            <el-option label="天津" value="TJ"/>
            <el-option label="重庆" value="CQ"/>
            <el-option label="河北" value="HE"/>
            <el-option label="山西" value="SX"/>
            <el-option label="辽宁" value="LN"/>
            <el-option label="吉林" value="JL"/>
            <el-option label="黑龙江" value="HL"/>
            <el-option label="江苏" value="JS"/>
            <el-option label="浙江" value="ZJ"/>
            <el-option label="安徽" value="AH"/>
            <el-option label="福建" value="FJ"/>
            <el-option label="江西" value="JX"/>
            <el-option label="山东" value="SD"/>
            <el-option label="河南" value="HA"/>
            <el-option label="湖北" value="HB"/>
            <el-option label="湖南" value="HN"/>
            <el-option label="广东" value="GD"/>
            <el-option label="广西" value="GX"/>
            <el-option label="海南" value="HI"/>
            <el-option label="四川" value="SC"/>
            <el-option label="贵州" value="GZ"/>
            <el-option label="云南" value="YN"/>
            <el-option label="西藏" value="XZ"/>
            <el-option label="陕西" value="SN"/>
            <el-option label="甘肃" value="GS"/>
            <el-option label="青海" value="QH"/>
            <el-option label="宁夏" value="NX"/>
            <el-option label="新疆" value="XJ"/>
            <el-option label="台湾" value="TW"/>
            <el-option label="香港" value="HK"/>
            <el-option label="澳门" value="MO"/>
          </el-select>
        </el-form-item>
        <el-form-item label="工号" prop="userworknum"> <!-- prop是验证规则属性 -->
          <el-input v-model="editUserForm.userworknum"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="editUserForm.password" type="password"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="useremail">
          <el-input v-model="editUserForm.useremail"></el-input>
        </el-form-item>
        <el-form-item label="手机" prop="userphonenum">
          <el-input v-model="editUserForm.userphonenum"></el-input>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer" class="dialog-footer">
      <el-button @click="editDialogVisible = false">取 消</el-button>
      <el-button type="primary" @click="updateUser">确 定</el-button></span>
    </el-dialog>
  </div>
</template>

<script>
import {Search} from "@element-plus/icons-vue";
import axios from "axios";
import zhCn from "element-plus/lib/locale/lang/zh-cn";
import {ElDialog} from "element-plus";

export default {
  name: "PmsUserList",
  computed: {
    zhCn() {
      return zhCn
    }
  },
  components: {Search, ElDialog},
  data() {
    const checkEmail = (rule, value, callback) => {
      //验证邮箱的正则表达式
      const regEmail = /^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;
      if (regEmail.test(value)) {
        return callback(); //合法邮箱
      }
      return callback(new Error("请输入合法的邮箱"));
    }
    const checkWorknum = (rule, value, callback) => {
      //验证工号的正则表达式
      const regWorknum = /^\d{5}$/;
      if (regWorknum.test(value)) {
        return callback(); //合法邮箱
      }
      return callback(new Error("请输入合法的工号"));
    }
    const checkMobile = (rule, value, callback) => {
      //验证手机号的正则表达式
      const regMobile = /^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}$/;
      if (regMobile.test(value)) {
        return callback(); //合法手机号
      }
      return callback(new Error("请输入合法的手机号"));
    }
    return {
      //获取用户列表的参数对象
      queryInfo: {
        query: "",
        pageNum: 1, // 分页默认从第一页开始
        pageSize: 10,// 默认每页显示n条数据
      },
      userlist: [],      //用户列表
      count: 0,      //总数据
      addDialogVisible: false, //控制添加用户对话框的显示与隐藏
      editDialogVisible: false, //控制修改用户对话框的显示与隐藏
      DeleteDialogVisible: false,// 控制删除用户对话框的显示与隐藏
      //添加用户表单数据
      addUserForm: {},
      //修改用户表单数据
      editUserForm: {},
      //表单验证规则
      addUserFormRules: {
        username: [{required: true, message: '请输入用户名', trigger: 'blur'}, {
          min: 3,
          max: 15,
          message: '用户名长度在3~15个字符',
          trigger: 'blur'
        }],
        usernicname: [{required: false, message: '请输入昵称', trigger: 'blur'}, {
          min: 3,
          max: 20,
          message: '用户名长度在3~20个字符',
          trigger: 'blur'
        }],
        userjob: [{required: false, message: '请选择工作岗位', trigger: 'blur'}],
        userbase: [{required: true, message: '请选择工作地点', trigger: 'blur'}],
        password: [{required: false, message: '请输入密码', trigger: 'blur'}, {
          min: 6,
          max: 20,
          message: '密码长度在6~20个字符',
          trigger: 'blur'
        }],
        useremail: [{required: true, message: '请输入邮箱', trigger: 'blur'}, {validator: checkEmail, trigger: 'blur'}],
        userphonenum: [{required: true, message: '请输入手机号', trigger: 'blur'}, {
          validator: checkMobile,
          trigger: 'blur'
        }],
        userworknum: [{required: true, message: '请输入工号', trigger: 'blur'}, {
          validator: checkWorknum,
          trigger: 'blur'
        }],
      },
      editUser: {},
    }
  },
  created() {
    this.getUserList();
  },
  methods: {
    // 监听 page size 改变的事件
    handleSizeChange(newSize) {
      this.queryInfo.pageSize = newSize //重新知道每页数量
      this.getUserList();
    },
    // 监听 页码值 改变的事件
    handleCurrentChange(newPage) {
      this.queryInfo.pageNum = newPage
      this.getUserList()
    },
    //对话框打开
    openAddDialog() {
      this.addDialogVisible = true;
    },
    //监听switch开关状态的改变
    // async userStateChange(userinfo) {
    //   const {data: res} = await axios.put(`update_user/${userinfo.id}`, {mg_state: userinfo.mg_state})
    //   if (res.code !== 0) {
    //     return this.$message.error('更新用户状态失败')
    //   }
    //   this.$message.success('更新用户状态成功')
    // },
    // 所有用户查询，搜索用户
    async getUserList() {
      if (this.queryInfo.query !== "") {
        try {
          const {data: res} = await axios.get(`/user/search?username=${this.queryInfo.query}`);
          if (res.code !== 0) {
            return this.$message.error('查询失败，没有此用户')
          }
          this.userlist = res.users;
        } catch (error) {
          return this.$message.error('查询失败，没有此用户')
        }
      } else {
        try {
          const {data: res} = await axios.get(`user/get?pageNum=${this.queryInfo.pageNum}&pageSize=${this.queryInfo.pageSize}`);
          if (res.code !== 0) {
            return this.$message.error('获取用户列表失败')
          }
          this.userlist = res.users;
          this.count = res.pagination.count;
        } catch (error) {
          return this.$message.error('获取用户列表失败')
        }
      }
    },
    //展示编辑用户的对话框
    async showEditDialog(username) {
      try {
        const response = await axios.get(`user/search?username=${username}`);
        const res = response.data;
        if (res && res.code === 0 && res.users && res.users.length > 0) {
          this.editDialogVisible = true;
          this.editUserForm = res.users[0];
          //console.log(this.editUserForm);
        } else {
          this.$message.error('未找到用户信息');
        }
      } catch (error) {
        console.error(error);
        this.$message.error('获取用户信息失败');
      }
    },
    //创建用户
    async createUser() {
      try {
        await this.$refs.addUserFormRef.validate(); // 表单验证
        const formData = new FormData();
        formData.append('username', this.addUserForm.username);
        formData.append('usernicname', this.addUserForm.usernicname);
        formData.append('userjob', this.addUserForm.userjob);
        formData.append('userbase', this.addUserForm.userbase);
        formData.append('userworknum', this.addUserForm.userworknum);
        formData.append('password', this.addUserForm.password);
        formData.append('useremail', this.addUserForm.useremail);
        formData.append('userphonenum', this.addUserForm.userphonenum);
        const {data: res} = await axios.post("/user/create", formData, {
          headers: {
            'Content-Type': 'multipart/form-data' // 设置请求的 Content-Type
          }
        }); // 发送创建用户的请求
        if (res.code !== 0) {
          this.$message.error(res.message || "创建用户失败");
          return;
        }
        this.$message.success("创建用户成功");
        this.addDialogVisible = false; // 关闭对话框
        this.$refs.addUserFormRef.resetFields(); // 重置表单
        this.getUserList(); // 刷新用户列表
      } catch (error) {
        this.$message.error("表单验证失败，请检查输入");
      }
    },
    //修改用户
    async updateUser() {
      try {
        await this.$refs.editUserFormRef.validate(); // 表单验证
        const formData = new FormData();
        formData.append('username', this.editUserForm.username);
        formData.append('usernicname', this.editUserForm.usernicname);
        formData.append('userjob', this.editUserForm.userjob);
        formData.append('userbase', this.editUserForm.userbase);
        formData.append('userworknum', this.editUserForm.userworknum);
        formData.append('password', this.editUserForm.password);
        formData.append('useremail', this.editUserForm.useremail);
        formData.append('userphonenum', this.editUserForm.userphonenum);
        const {data: res} = await axios.put(`/user/update/${this.editUserForm.id}`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data' // 设置请求的 Content-Type
          }
        }); // 发送创建用户的请求
        if (res.code !== 0) {
          this.$message.error(res.message || "更新用户失败");
          return;
        }
        this.$message.success("更新用户成功");
        this.editDialogVisible = false; // 关闭对话框
        this.$refs.editUserFormRef.resetFields(); // 重置表单
        this.getUserList(); // 刷新用户列表
      } catch (error) {
        this.$message.error("表单验证失败，请检查输入");
      }
    },
    // 展示删除用户对话框
    showDeleteDialog(id)
    {
      this.$confirm('确认删除该用户嘛？', '提示', {
        confirmButtonText: "确认",
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        //确认删除
        this.delete_user(id);
      }).catch(() => {
        //取消不执行所有操作
      });
    },
    //删除用户
    delete_user(id) {
      try {
        axios.delete(`user/delete/${id}`)
            .then(response => {
              const res = response.data;
              if (res.code === 0) {
                this.$message.success('删除用户成功');
                this.getUserList(); // 刷新用户列表
              } else {
                this.$message.error(res.msg || '删除用户失败');
              }
            })
            .catch(error => {
              console.error(error);
              this.$message.error('删除用户失败');
            });
      } catch (error) {
        console.error(error);
        this.$message.error('删除用户失败');
      }
    }
  }
}
</script>

<style scoped>
/*全局样式*/
html
body
#app {
  height: 100%;
  margin: 0;
  padding: 0;
}

.el-breadcrumb {
  margin-bottom: 15px;
  font-size: 12px;
}

.el-card {
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.15) !important;
}

.search-area {
  margin-bottom: 20px;
}

</style>