<template xmlns="http://www.w3.org/1999/html" @>
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
            <el-button type="info" @click="showMoreInfo(scope.row)">
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
          <el-button type="primary" @click="showEditDialog(scope.row.id)">
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
  <el-dialog v-model="addDialogVisible" title="添加项目" width="50%">
    <!-- 内容主体区 -->
    <el-form ref="addProjectRef" :model="addProjectForm" :rules="addProjectFormRules" label-width="100px">
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
                     :value="product.product_name + '-'+product.product_version+'-'+product.product_install_method"/>
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
      <el-form-item label="操作人" prop="project_update_user"> <!-- prop是验证规则属性 -->
        <el-select v-model="addProjectForm.project_update_user" placeholder="点击选择">
          <el-option v-for="user in userList" :key="user.id" :label="user.username" :value="user.username"/>
        </el-select>
      </el-form-item>
      <el-form-item label="更新文档" prop="project_update_file">
        <el-tooltip placement="top">
          <template #content>
            (1):文件格式为时间+产品+项目+文档名(示例：20230909-bot3.0-华夏卡部署文档.pdf);<br>
            (2):支持文件类型：.PDF;"
          </template>
          <el-upload
              :auto-upload="false"
              :on-change="handleFileChange"
              name="file"
          >
            <el-button size="small" type="primary">
              点击上传文件
            </el-button>
          </el-upload>
        </el-tooltip>
      </el-form-item>
      <el-form-item label="IVC版本" prop="project_ivc"> <!-- prop是验证规则属性 -->
        <el-select v-model="addProjectForm.project_ivc" placeholder="点击选择">
          <el-option label="追一自研" value="追一自研"/>
          <el-option label="其他" value="其他" @click="openInputPopup('IVC','create')"/>
        </el-select>
      </el-form-item>
      <el-form-item label="数据库版本" prop="project_db"> <!-- prop是验证规则属性 -->
        <el-select v-model="addProjectForm.project_db" placeholder="点击选择">
          <el-option label="追一自研" value="追一自研"/>
          <el-option label="其他" value="其他" @click="openInputPopup('DB','create')"/>
        </el-select>
      </el-form-item>
      <el-form-item label="中间件版本" prop="project_middleware"> <!-- prop是验证规则属性 -->
        <el-select v-model="addProjectForm.project_middleware" placeholder="点击选择">
          <el-option label="追一自研" value="追一自研"/>
          <el-option label="其他" value="其他" @click="openInputPopup('Middleware','create')"/>
        </el-select>
      </el-form-item>
    </el-form>
    <!-- 底部区 -->
    <span slot="footer" class="dialog-footer">
      <el-button @click="addDialogVisible = false">取 消</el-button>
      <el-button type="primary" @click="createProject">确 定</el-button></span>
  </el-dialog>
  <!--  显示更多信息-->
  <el-dialog v-model="showMoreDialog" title="所有信息" width="50%">
    <!-- 显示项目的更多信息 -->
    <div class="more-info-dialog">
      <p class="info-line">项目名称: {{ selectedProject.project_name }}</p>
      <p class="info-line">项目编号: {{ selectedProject.project_num }}</p>
      <p class="info-line">项目所属区域: {{ selectedProject.project_base }}</p>
      <p class="info-line">项目所属PM: {{ selectedProject.project_owner }}</p>
      <p class="info-line">项目驻场TM: {{ selectedProject.project_resident }}</p>
      <p class="info-line">项目部署产品(名称-版本-部署方式): {{ selectedProject.project_product }}</p>
      <p class="info-line">项目更新日期: {{ selectedProject.project_update_time }}</p>
      <p class="info-line">项目更新操作用户: {{ selectedProject.project_update_user }}</p>
      <!-- 文件列表展示 -->
      <p class="info-line">文件列表:
        <router-link
            :to="{ name: 'project_type', params: { project_type: 'main', project_name: selectedProject.project_name } }">
          文件列表
        </router-link>
      </p>
      <p class="info-line">项目所使用IVC: {{ selectedProject.project_ivc }}</p>
      <p class="info-line">项目所使用数据库: {{ selectedProject.project_db }}</p>
      <p class="info-line">项目所使用中间件: {{ selectedProject.project_middleware }}</p>
    </div>
    <div class="close-button-wrapper">
       <span slot="footer" class="dialog-footer">
    <el-button type="info" @click="showMoreDialog = false">关闭</el-button>
  </span>
    </div>
  </el-dialog>
  <!--  修改项目弹窗-->
  <el-dialog v-model="editDialogVisible" title="修改项目" width="50%">
    <!-- 内容主体区 -->
    <el-form ref="editProjectFormRef" :model="editProjectForm" :rules="addProjectFormRules" label-position="top">
      <el-form-item label="名称" prop="project_name"> <!-- prop是验证规则属性 -->
        <el-input v-model="editProjectForm.project_name" disabled></el-input>
      </el-form-item>
      <el-form-item label="区域" prop="project_base"> <!-- prop是验证规则属性 -->
        <el-select v-model="editProjectForm.project_base" placeholder="editProjectForm.project_base">
          <el-option label="北区" value="北区"/>
          <el-option label="东区" value="东区"/>
          <el-option label="南区" value="南区"/>
        </el-select>
      </el-form-item>
      <el-form-item label="编号" prop="project_num"> <!-- prop是验证规则属性 -->
        <el-input v-model="editProjectForm.project_num" disabled></el-input>
      </el-form-item>
      <el-form-item label="PM" prop="project_owner"> <!-- prop是验证规则属性 -->
        <el-select v-model="editProjectForm.project_owner" placeholder="editProjectForm.project_owner">
          <el-option v-for="tm in tmList" :key="tm.id" :label="tm.username" :value="tm.username"/>
        </el-select>
      </el-form-item>
      <el-form-item label="TM" prop="project_resident"> <!-- prop是验证规则属性 -->
        <el-select v-model="editProjectForm.project_resident" placeholder="editProjectForm.project_resident">
          <el-option v-for="tm in tmList" :key="tm.id" :label="tm.username" :value="tm.username"/>
        </el-select>
      </el-form-item>
      <el-form-item label="产品" prop="project_product"> <!-- prop是验证规则属性 -->
        <el-select v-model="editProjectForm.project_product" placeholder="点击选择">
          <el-option v-for="product in productList" :key="product.id"
                     :label="product.product_name + '-'+product.product_version+'-'+product.product_install_method"
                     :value="product.product_name + '-'+product.product_version+'-'+product.product_install_method"/>
        </el-select>
      </el-form-item>
      <el-form-item label="更新日期" prop="project_update_time"> <!-- prop是验证规则属性 -->
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
      <el-form-item label="操作用户" prop="project_update_user"> <!-- prop是验证规则属性 -->
        <el-select v-model="editProjectForm.project_update_user" placeholder="点击选择">
          <el-option v-for="user in userList" :key="user.id" :label="user.username" :value="user.username"/>
        </el-select>
      </el-form-item>
      <el-form-item label="文档" prop="project_name"> <!-- prop是验证规则属性 -->
        <el-tooltip placement="top">
          <template #content>
            (1):文件格式为时间+产品+项目+文档名(示例：20230909-bot3.0-华夏卡部署文档.pdf);<br>
            (2):支持文件类型：.PDF;"
          </template>
          <el-upload
              :auto-upload="false"
              :on-change="handleFileChange"
              name="file"
          >
            <el-button size="small" type="primary">
              点击上传文件
            </el-button>
          </el-upload>
        </el-tooltip>
      </el-form-item>
      <el-form-item label="IVC" prop="project_ivc"> <!-- prop是验证规则属性 -->
        <el-select v-model="editProjectForm.project_ivc" placeholder="点击选择">
          <el-option label="追一自研" value="追一自研"/>
          <el-option label="其他" value="其他" @click="openInputPopup('IVC','update')"/>
        </el-select>
      </el-form-item>
      <el-form-item label="数据库" prop="project_db"> <!-- prop是验证规则属性 -->
        <el-select v-model="editProjectForm.project_db" placeholder="点击选择">
          <el-option label="追一自研" value="追一自研"/>
          <el-option label="其他" value="其他" @click="openInputPopup('DB','update')"/>
        </el-select>
      </el-form-item>
      <el-form-item label="中间件" prop="project_middleware"> <!-- prop是验证规则属性 -->
        <el-select v-model="editProjectForm.project_middleware" placeholder="点击选择">
          <el-option label="追一自研" value="追一自研"/>
          <el-option label="其他" value="其他" @click="openInputPopup('Middleware','update')"/>
        </el-select>
      </el-form-item>
    </el-form>
    <!-- 底部区 -->
    <span slot="footer" class="dialog-footer">
      <el-button @click="editDialogVisible = false">取 消</el-button>
      <el-button type="primary" @click="updateProject">确 定</el-button></span>
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
  components: {Search, ElDialog, ElDatePicker, MoreFilled},
  data() {
    return {
      showTooltip: false,//提示
      uploadedFiles: [], // 用于存储上传的文件
      //打开更多信息弹窗
      showMoreDialog: false,
      fileToUpload: null,
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
      addProjectForm: {
        project_ivc: '追一自研',         // IVC默认值
        project_db: '追一自研',          // 数据库默认值
        project_middleware: '追一自研',  // 中间件默认值
      },
      //表单验证规则
      addProjectFormRules: {
        project_name: [{required: true, message: '请选择项目名字', trigger: 'blur'}],
        project_base: [{required: true, message: '请选择项目所属区域', trigger: 'blur'}],
        project_num: [{required: true, message: '请选择项目编号', trigger: 'blur'}],
        project_owner: [{required: true, message: '请选择项目所属PM', trigger: 'blur'}],
        project_resident: [{required: true, message: '请选择项目驻场TM', trigger: 'blur'}],
        project_product: [{required: true, message: '请选择项目部署产品', trigger: 'blur'}],
        project_update_time: [{required: true, message: '请选择更新时间', trigger: 'blur'}],
        project_update_user: [{required: true, message: '请选择更新用户', trigger: 'blur'}],

      },
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
      //修改项目表单数据
      editProjectForm: {},
      //文件上传
      uploadDialogVisible: false,
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
    //操作记录
    operationHistory(content, project_name, file_name) {
      const username = sessionStorage.getItem("username")
      const formData = new FormData();
      formData.append('file_name', file_name)
      formData.append('user', username);
      formData.append('content', content);
      formData.append('operation_type', "用户管理");
      formData.append('project_name', project_name)
      axios.post('/history/record_user_operation', formData, {
        headers: {
          'Content-Type': 'multipart/form-data' // 设置请求的 Content-Type
        }
      })
    },
    //所有信息展示
    showMoreInfo(project) {
      this.selectedProject = project;
      this.showMoreDialog = true;
    },
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
        this.delete_project(id);
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
    //打开输入弹窗
    openInputPopup(optionType, operationType) {
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
      }).then(({value}) => {
        if (operationType === 'create') {
          this.addProjectForm[valueKey] = value; // 创建操作赋值
        } else if (operationType === 'update') {
          this.editProjectForm[valueKey] = value; // 更新操作赋值
        }
      }).catch(() => {
        // 取消输入
      });
    },
    // 处理文件上传变化
    handleFileChange(file) {
      this.fileToUpload = file.raw;
    },
    //查询所有项目 搜索项目
    async getProjectsList() {
      if (this.queryInfo.query !== "") {
        try {
          const {data: res} = await axios.get(`mainProjects/search?project_name=${this.queryInfo.query}`);
          if (res.code !== 0) {
            return this.$message.error('查询失败，没有此项目')
          }
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
          this.projectsList = res.projects
          this.count = res.pagination.count
        } catch (error) {
          return this.$message.error('获取项目列表失败')
        }
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
    //执行上传逻辑
    async executeUpload() {
      const projectName = this.projectNameToUpload; // 使用项目名称变量
      if (!projectName) {
        console.error("projectName 不存在");
        return;
      }

      // 将项目名 project_name 传递给接口
      const formData = new FormData();
      formData.append("project_name", projectName);
      formData.append("directory_type", "main");

      // 将文件放入请求体
      if (this.fileToUpload) {
        const fileName = this.fileToUpload.name;
        const uploadUrl = `/file/upload`; // 上传接口的URL
        const chunkSize = 1024 * 1024; // 分块大小，这里设置为1MB，可以根据需求调整

        // 分块上传逻辑
        let start = 0;
        while (start < this.fileToUpload.size) {
          const chunk = this.fileToUpload.slice(start, start + chunkSize);
          formData.append("file", chunk, fileName); // 指定文件名
          const headers = {
            'Content-Type': 'multipart/form-data; charset=UTF-8', // 设置请求的 Content-Type
          };
          try {
            const response = await axios.post(uploadUrl, formData, {headers});
            if (response.status === 200) {
              // 上传成功的逻辑
              console.log(`上传了分块：${start}-${start + chunk.size}`);
            } else {
              console.error("上传文件失败了");
            }
          } catch (error) {
            // 异常处理
            console.error("上传文件出错", error);
            break; // 如果出现错误，跳出循环
          }

          start += chunkSize;
        }

        this.addDialogVisible = false; // 关闭弹窗
        this.operationHistory("上传了一个文件", projectName, fileName);
      }
    },
    // 创建项目
    async createProject() {
      try {
        await this.$refs.addProjectRef.validate(); // 表单验证
        this.projectNameToUpload = this.addProjectForm.project_name; // 提取项目名称
        const project_name = this.projectNameToUpload
        const formData = new FormData();
        formData.append('project_name', this.addProjectForm.project_name);
        formData.append('project_base', this.addProjectForm.project_base);
        formData.append('project_num', this.addProjectForm.project_num);
        formData.append('project_owner', this.addProjectForm.project_owner);
        formData.append('project_resident', this.addProjectForm.project_resident);
        formData.append('project_product', this.addProjectForm.project_product);
        formData.append('project_update_time', this.addProjectForm.project_update_time);
        formData.append('project_update_user', this.addProjectForm.project_update_user);
        formData.append('project_update_file', "文件列表");
        formData.append('project_ivc', this.addProjectForm.project_ivc);
        formData.append('project_db', this.addProjectForm.project_db);
        formData.append('project_middleware', this.addProjectForm.project_middleware);

        const {data: res} = await axios.post("/mainProjects/create", formData, {
          headers: {
            'Content-Type': 'multipart/form-data' // 设置请求的 Content-Type
          }
        }); // 发送创建产品的请求
        if (res.code !== 0) {
          this.$message.error(res.message || "创建项目失败");
          return;
        }
        // 定义一个正则表达式来匹配文件名的标准格式
        const fileNameRegex = /^(\d{8}-[a-zA-Z]+[\d.]+-[\u4e00-\u9fa5a-zA-Z]+)\.pdf$/;
        const fileName = this.fileToUpload.name;
        this.$message.success("创建项目成功");
        // 检查文件名是否符合标准
        this.$refs.addProjectRef.resetFields(); // 重置表单
        await this.getProjectsList(); // 刷新产品列表
        this.addDialogVisible = false; // 关闭对话框
        this.operationHistory("创建了一个主线项目", project_name) //记录操作
        if (!fileNameRegex.test(fileName)) {
          this.$message.error(res.message || "文件名不符合标准格式,请从项目修改页面重新上传");
          return;
        }
      } catch (error) {
        console.error(error)
        this.$message.error("表单验证失败，请检查输入");
        this.openAddDialog()
      }
      this.executeUpload();
    },
    //展示编辑用户的对话框
    async showEditDialog(id) {
      try {
        const response = await axios.get(`mainProjects/search?id=${id}`);
        const res = response.data;
        if (res && res.code === 0 && res.projects) {
          this.editDialogVisible = true;
          this.editProjectForm = res.projects[0];
        } else {
          this.$message.error('未找到项目信息');
        }
      } catch (error) {
        console.error(error);
        this.$message.error('获取用户项目失败');
      }
    },
    //修改项目
    async updateProject() {
      try {
        await this.$refs.editProjectFormRef.validate(); // 表单验证
        this.projectNameToUpload = this.editProjectForm.project_name; // 提取项目名称
        const project_name = this.projectNameToUpload
        const formData = new FormData();
        formData.append('project_name', this.editProjectForm.project_name);
        formData.append('project_base', this.editProjectForm.project_base);
        formData.append('project_num', this.editProjectForm.project_num);
        formData.append('project_owner', this.editProjectForm.project_owner);
        formData.append('project_resident', this.editProjectForm.project_resident);
        formData.append('project_product', this.editProjectForm.project_product);
        formData.append('project_update_time', this.editProjectForm.project_update_time);
        formData.append('project_resident', this.editProjectForm.project_resident);
        formData.append('project_update_file', "文件列表");
        formData.append('project_ivc', this.editProjectForm.project_ivc);
        formData.append('project_db', this.editProjectForm.project_db);
        formData.append('project_middleware', this.editProjectForm.project_middleware);
        const {data: res} = await axios.put(`/mainProjects/update/${this.editProjectForm.id}`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data' // 设置请求的 Content-Type
          }
        }); // 发送创建用户的请求
        if (res.code !== 0) {
          this.$message.error(res.message || "更新项目失败");
          return;
        }
        this.$message.success("更新项目成功");
        this.$refs.editProjectFormRef.resetFields(); // 重置表单
        this.editDialogVisible = false; // 关闭对话框
        this.getProjectsList(); // 刷新用户列表
        this.operationHistory("更新了一个主线项目", project_name)
        const fileNameRegex = /^(\d{8}-[a-zA-Z]+[\d.]+-[\u4e00-\u9fa5a-zA-Z]+)\.pdf$/;
        const fileName = this.fileToUpload.name;
        if (!fileNameRegex.test(fileName)) {
          this.$message.error(res.message || "文件名不符合标准格式,请从项目修改页面重新上传");
          return;
        }

      } catch (error) {
        this.$message.error("表单验证失败，请检查输入");
      }
      this.executeUpload()
    },
    //删除项目
    async delete_project(id) {
      // 先向服务器请求获取项目的详细信息
      const response = await axios.get(`mainProjects/search?id=${id}`);
      const project = response.data; // 获取项目信息，包括名称
      const project_name = project.projects[0].project_name
      try {
        axios.delete(`mainProjects/delete/${id}`)
            .then(response => {
              const res = response.data;
              if (res.code === 0) {
                this.$message.success('删除项目成功');
                this.getProjectsList(); // 刷新项目列表
                this.operationHistory("删除了一个主线项目", project_name)
              } else {
                this.$message.error(res.msg || '删除项目失败');
              }
            })
            .catch(error => {
              console.error(error);
              this.$message.error('删除项目失败');
            });
      } catch (error) {
        console.error(error);
        this.$message.error('删除项目失败');
      }
    }
  },
}
</script>

<style scoped>

#app {
  height: 100%;
  margin: 0;
  padding: 0;
}

.el-tooltip__content {
  white-space: pre-line;
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

.more-info-dialog {
  border: 2px solid #ccc; /* 边框 */
  background-color: rgba(0, 0, 0, 0.5); /* 暗底背景颜色 */
  padding: 1px; /* 可选：添加内边距 */
  color: #fff; /* 可选：设置文本颜色为白色 */
  margin-top: -20px; /* 调整上边距 */
}

.info-line {
  line-height: 1.5; /* Adjust the line height as needed */
  margin: 8px 0; /* Add margin above and below each line */
}

.close-button-wrapper {
  margin-top: 10px; /* 设置顶部间距 */
}
</style>