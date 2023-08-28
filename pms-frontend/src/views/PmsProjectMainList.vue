<template>
  <!-- 面包屑导航 -->
  <el-breadcrumb separator-class="el-icon-arrow-right">
    <el-breadcrumb-item :to="'/home'">首页</el-breadcrumb-item>
    <el-breadcrumb-item :to="''">项目管理</el-breadcrumb-item>
    <el-breadcrumb-item :to="'/mainProjects'">主线</el-breadcrumb-item>
    <el-breadcrumb-item>项目列表</el-breadcrumb-item>
  </el-breadcrumb>
  <el-card>
    <!-- 搜索与添加区域 -->
    <div class="search-area">
      <el-row :gutter="20">
        <!--        指定每个栏位为20-->
        <el-col :span="20">
          <el-input v-model='queryInfo.query' clearable placeholder="请输入项目名称" @clear="getProjectsList">
            <template #append>
              <el-button slot="append" @click="getProjectsList">
                <el-icon>
                  <Search/>
                </el-icon>
              </el-button>
            </template>
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary" @click="openAddDialog">添加项目</el-button>
        </el-col>
      </el-row>
    </div>
    <!--      项目列表区域-->
    <el-table :data="projectsList" border stripe>
      <el-table-column type="index"></el-table-column>
      <el-table-column label="项目名称" prop="project_name"></el-table-column>
      <el-table-column label="区域" prop="project_base"></el-table-column>
      <el-table-column label="编号" prop="project_num"></el-table-column>
      <el-table-column label="PM" prop="project_owner"></el-table-column>
      <el-table-column label="TM" prop="project_resident"></el-table-column>
      <el-table-column label="产品" prop="project_product"></el-table-column>
      <el-table-column label="更新日期" prop="project_update_time"></el-table-column>
      <el-table-column header-align="center" label="更多信息" width="150px">
        <template v-slot="scope">
          <div style="display: flex; justify-content: center; align-items: center;">
            <el-button type="info" @click="">
              <el-icon>
                <MoreFilled/>
              </el-icon>
            </el-button>
          </div>
        </template>
      </el-table-column>
      <el-table-column header-align="center" label="操作" width="150px">
        <template v-slot="scope">
          <!-- 修改按钮 -->
          <el-button type="primary" @click="">
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
  <!-- 添加项目弹窗 -->
  <el-dialog v-model="addDialogVisible" title="添加产品" width="50%">
    <!-- 内容主体区 -->
    <el-form ref="addProjectRef" :model="addProjectForm" label-width="100px">
      <el-form-item label="项目名" prop="project_name"> <!-- prop是验证规则属性 -->
        <el-input v-model="addProjectForm.project_name"></el-input>
      </el-form-item>
      <el-form-item label="项目所属区域" prop="project_base"> <!-- prop是验证规则属性 -->
        <el-select v-model="addProjectForm.project_base" placeholder="点击选择">
          <el-option label="北区" value="北区"/>
          <el-option label="东区" value="东区"/>
          <el-option label="南区" value="南区"/>
        </el-select>
      </el-form-item>
      <el-form-item label="项目编号" prop="project_num"> <!-- prop是验证规则属性 -->
        <el-input v-model="addProjectForm.project_num"></el-input>
      </el-form-item>
      <el-form-item label="所属PM" prop="project_owner"> <!-- prop是验证规则属性 -->
        <el-select v-model="addProjectForm.project_owner" placeholder="点击选择">
          <el-option v-for="pm in pmList" :key="pm.id" :label="pm.username" :value="pm.username"/>
        </el-select>
      </el-form-item>
      <el-form-item label="驻场TM" prop="project_resident"> <!-- prop是验证规则属性 -->
        <el-select v-model="addProjectForm.project_resident" placeholder="点击选择">
          <el-option v-for="tm in tmList" :key="tm.id" :label="tm.username" :value="tm.username"/>
        </el-select>
      </el-form-item>
      <el-form-item label="部署产品" prop="project_product"> <!-- prop是验证规则属性 -->
        <el-select v-model="addProjectForm.project_product" placeholder="点击选择">
          <el-option v-for="product in productList" :key="product.id"
                     :label="product.product_name + '-'+product.product_version+'-'+product.product_install_method"
                     :value="product.product_name"/>
        </el-select>
      </el-form-item>
      <el-form-item label="更新时间" prop="project_update_time">
        <el-config-provider :locale="locale">
          <el-date-picker
              v-model="addProjectForm.project_update_time"
              :locale="locale"
              format="YYYY/MM/DD"
              placeholder="点击选择"
              type="date"
              value-format="YYYY-MM-DD"
          ></el-date-picker>
        </el-config-provider>
      </el-form-item>
      <el-form-item label="操作人" prop="project_resident"> <!-- prop是验证规则属性 -->
        <el-select v-model="addProjectForm.project_update_user" placeholder="点击选择">
          <el-option v-for="user in userList" :key="user.id" :label="user.username" :value="user.username"/>
        </el-select>
      </el-form-item>
      <el-form-item label="更新文档" prop="project_base"> <!-- prop是验证规则属性 -->
        <el-select v-model="addProjectForm.project_base" placeholder="点击选择">
          <el-option label="北区" value="北区"/>
        </el-select>
      </el-form-item>
      <el-form-item label="IVC版本" prop="project_ivc"> <!-- prop是验证规则属性 -->
        <el-select v-model="addProjectForm.project_ivc" placeholder="点击选择">
          <el-option label="追一自研" value="追一自研"/>
          <el-option label="其他" value="其他" @click="openInputPopup('IVC')"/>
        </el-select>
      </el-form-item>
      <el-form-item label="数据库版本" prop="project_db"> <!-- prop是验证规则属性 -->
        <el-select v-model="addProjectForm.project_db" placeholder="点击选择">
          <el-option label="追一自研" value="追一自研"/>
          <el-option label="其他" value="其他" @click="openInputPopup('DB')"/>
        </el-select>
      </el-form-item>
      <el-form-item label="中间件版本" prop="project_middleware"> <!-- prop是验证规则属性 -->
        <el-select v-model="addProjectForm.project_middleware" placeholder="点击选择">
          <el-option label="追一自研" value="追一自研"/>
          <el-option label="其他" value="其他" @click="openInputPopup('Middleware')"/>
        </el-select>
      </el-form-item>
    </el-form>
    <!-- 底部区 -->
    <span slot="footer" class="dialog-footer">
      <el-button @click="addDialogVisible = false">取 消</el-button>
      <el-button type="primary" @click="">确 定</el-button></span>
  </el-dialog>
</template>

<script>
import {MoreFilled, Search} from "@element-plus/icons-vue";
import axios from "axios";
import zhCn from "element-plus/lib/locale/lang/zh-cn";
import {ElDatePicker, ElDialog} from "element-plus";

export default {
  setup() {
    return {
      locale: zhCn,
    }
  },
  name: "PmsProjectList",
  computed: {
    zhCn() {
      return zhCn;
    },
  },
  components: {MoreFilled, Search, ElDialog, ElDatePicker},
  data() {
    return {
      //获取项目列表的参数对象
      queryInfo: {
        query: "",
        // 分页默认从第一页开始
        pageNum: 1,
        // 默认每页显示n条数据
        pageSize: 10,
      },
      //总数据
      count: 0,
      addDialogVisible: false, //控制添加项目对话框的显示与隐藏
      editDialogVisible: false, //控制修改项目对话框的显示与隐藏
      DeleteDialogVisible: false,// 控制删除项目对话框的显示与隐藏
      //添加项目表单数据
      addProjectForm: {},
      //表单验证规则
      // addProductFormRules: {
      //   product_name: [{required: true, message: '请选择项目名字', trigger: 'blur'}],
      //   product_version: [{required: true, message: '请选择项目版本', trigger: 'blur'}],
      //   product_install_method: [{required: false, message: '请选择项目部署方式', trigger: 'blur'}],
      // },
      //存储所有PM数据
      pmList: [],
      //存储所有TM数据
      tmList: [],
      //存储所有产品数据
      productList: [],
      //存储时间
      updateTime: '',
      //所有用户
      userList: [],
      //项目列表
      projectsList: [],
    }
  },
  created() {
    this.getProjectsList();
    this.getPmList();
    this.getTmList();
    this.getProductList();
    this.getAllUser();
  },
  methods: {
    //对话框打开
    openAddDialog() {
      this.addDialogVisible = true;
    },
    // 展示删除项目对话框
    showDeleteDialog(id) {
      this.$confirm('确认删除该项目嘛？', '提示', {
        confirmButtonText: "确认",
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        //确认删除
        this.delete_product(id);
      }).catch(() => {
        //取消不执行所有操作
      });
    },
    // 监听 page size 改变的事件
    handleSizeChange(newSize) {
      this.queryInfo.pageSize = newSize //重新知道每页数量
      this.getProjectsList();
    },
    // 监听 页码值 改变的事件
    handleCurrentChange(newPage) {
      this.queryInfo.pageNum = newPage
      this.getProjectsList()
    },
    //查询所有项目 搜索项目
    async getProjectsList() {
      if (this.queryInfo.query !== "") {
        // console.log(this.queryInfo.query)
        try {
          const {data: res} = await axios.get(`mainProjects/search?project_name=${this.queryInfo.query}`);
          if (res.code !== 0) {
            return this.$message.error('查询失败，没有此项目')
          }
          //console.log(res)
          this.projectsList = res.projects
        } catch (error) {
          return this.$message.error('查询失败，没有此项目')
        }
      } else {
        try {
          const {data: res} = await axios.get(`/mainProjects/list?pageNum=${this.queryInfo.pageNum}&pageSize=${this.queryInfo.pageSize}`);
          if (res.code !== 0) {
            return this.$message.error('获取项目列表失败')
          }
          //console.log(res)
          this.projectsList = res.projects
          this.count = res.pagination.count
          //console.log(this.projectsList)
        } catch (error) {
          return this.$message.error('获取项目列表失败')
        }
      }
    },
    //创建项目
    async createProject() {
      try {
        await this.$refs.addPorjectRef.validate(); // 表单验证
        const formData = new FormData();
        formData.append('project_name', this.addProjectForm.project_name);

        const {data: res} = await axios.post("/mainProjects/create", formData, {
          headers: {
            'Content-Type': 'multipart/form-data' // 设置请求的 Content-Type
          }
        }); // 发送创建产品的请求
        if (res.code !== 0) {
          this.$message.error(res.message || "创建产品失败");
          return;
        }
        this.$message.success("创建产品成功");
        this.addDialogVisible = false; // 关闭对话框
        this.$refs.addProjectFormFef.resetFields(); // 重置表单
        this.getProjectsList(); // 刷新产品列表
      } catch (error) {
        this.$message.error("表单验证失败，请检查输入");
      }
    },
    //查询所有PM
    async getPmList() {
      try {
        const {data} = await axios.get('/user/pms');
        if (data.code != 0) {
          return this.$message.error("获取所有PM失败");
        }
        this.pmList = data.users;
      } catch (errro) {
        this.$message.error("获取所有PM失败");
      }
    },
    //查询所TM
    async getTmList() {
      try {
        const {data} = await axios.get('/user/tms');
        if (data.code != 0) {
          return this.$message.error("获取所有TM失败");
        }
        this.tmList = data.users;
      } catch (errro) {
        this.$message.error("获取所有TM失败");
      }
    },
    //查询所有产品
    async getProductList() {
      try {
        const {data} = await axios.get('/products/list');
        if (data.code != 0) {
          return this.$message.error("获取所有产品失败");
        }
        this.productList = data.products;
      } catch (errro) {
        this.$message.error("获取所有产品失败");
      }
    },
    //查询所有用户
    async getAllUser() {
      try {
        const {data} = await axios.get('/user/get');
        if (data.code != 0) {
          return this.$message.error("获取所有用户失败");
        }
        this.userList = data.users;
      } catch (errro) {
        this.$message.error("获取所有用户失败");
      }
    },
    //打开输入弹窗
    openInputPopup(optionType) {
    let title = ''; // 弹窗标题
    let valueKey = ''; // 弹窗输入值对应的属性名
    switch (optionType) {
      case 'IVC':
        title = 'IVC版本';
        valueKey = 'project_ivc';
        break;
      case 'DB':
        title = '数据库版本';
        valueKey = 'project_db';
        break;
      case 'Middleware':
        title = '中间件版本';
        valueKey = 'project_middleware';
        break;
    }

    this.$prompt(`请输入${title}`, '输入', {
      confirmButtonText: '确定',
      cancelButtonText: '取消'
    }).then(({ value }) => {
      this.addProjectForm[valueKey] = value;
    }).catch(() => {
      // 取消输入
    });
  },

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
  box-shadow: 0 2px 1px rgba(0, 0, 0, 0.15) !important;
}

.search-area {
  margin-bottom: 20px;
}
</style>