<template>
  <!-- 面包屑导航 -->
  <el-breadcrumb separator-class="el-icon-arrow-right">
    <el-breadcrumb-item :to="'/home'">首页</el-breadcrumb-item>
    <el-breadcrumb-item :to="'/products'">产品管理</el-breadcrumb-item>
    <el-breadcrumb-item>产品列表</el-breadcrumb-item>
  </el-breadcrumb>

  <el-card>
    <!-- 搜索与添加区域 -->
    <div class="search-area">
      <el-row :gutter="20">
        <!--        指定每个栏位为20-->
        <el-col :span="20">
          <el-input v-model='queryInfo.query' clearable placeholder="请输入产品名称" @clear="getProductsList">
            <template #append>
              <el-button slot="append" @click="getProductsList">
                <el-icon>
                  <Search/>
                </el-icon>
              </el-button>
            </template>
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary" @click="openAddDialog">添加产品</el-button>
        </el-col>
      </el-row>
    </div>
    <!--      产品列表区域-->
    <el-table :data="productsList" border stripe>
      <el-table-column type="index"></el-table-column>
      <el-table-column label="产品名称" prop="product_name"></el-table-column>
      <el-table-column label="部署版本" prop="product_version"></el-table-column>
      <el-table-column label="部署方式" prop="product_install_method"></el-table-column>
      <el-table-column label="备注" prop="product_notes"></el-table-column>
      <el-table-column label="操作" width="180px">
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
  <!-- 添加用户弹窗 -->
  <el-dialog v-model="addDialogVisible" title="添加产品" width="50%">
    <!-- 内容主体区 -->
    <el-form ref="addProductFormRef" :model="addProductForm" :rules="addProductFormRules" label-width="120px">
      <el-form-item label="产品名称" prop="product_name"> <!-- prop是验证规则属性 -->
        <el-select v-model="addProductForm.product_name" placeholder="点击选择">
          <el-option label="Bot" value="Bot"/>
          <el-option label="Call" value="Call"/>
          <el-option label="See" value="See"/>
          <el-option label="Pal" value="Pal"/>
          <el-option label="Learn" value="Learn"/>
          <el-option label="Ivc" value="Ivc"/>
          <el-option label="Aiforce" value="Aiforce"/>
        </el-select>
      </el-form-item>
      <el-form-item label="产品版本" prop="product_version">
        <el-row :gutter="20">
          <el-col :span="20">
            <el-select v-model="selectedMajorVersion" placeholder="选择大版本" @change="updateProductVersion">
              <el-option v-for="majorVersion in majorVersions" :key="majorVersion" :label="majorVersion"
                         :value="majorVersion"></el-option>
            </el-select>
          </el-col>
          <el-col :span="20">
            <el-select v-model="selectedMinorVersion" placeholder="选择小版本" @change="updateProductVersion">
              <el-option v-for="minorVersion in minorVersions" :key="minorVersion" :label="minorVersion"
                         :value="minorVersion"></el-option>
            </el-select>
          </el-col>
          <el-col :span="20">
            <el-select v-model="selectedPatchVersion" placeholder="选择修订版本" @change="updateProductVersion">
              <el-option v-for="patchVersion in patchVersions" :key="patchVersion" :label="patchVersion"
                         :value="patchVersion"></el-option>
            </el-select>
          </el-col>
          <el-col :span="10">
            <span>{{ selectedMajorVersion + '.' + selectedMinorVersion + '.' + selectedPatchVersion }}</span>
          </el-col>
        </el-row>
      </el-form-item>
      <el-form-item label="产品部署方式" prop="product_install_method"> <!-- prop是验证规则属性 -->
        <el-select v-model="addProductForm.product_install_method" placeholder="点击选择(默认为未知)">
          <el-option label="Docker" value="Docker"/>
          <el-option label="Tar" value="Tar"/>
          <el-option label="Kubernetes(k8s)" value="k8s"/>
        </el-select>
      </el-form-item>
      <el-form-item label="产品备注" prop="product_notes"> <!-- prop是验证规则属性 -->
        <el-input v-model="addProductForm.product_notes" placeholder="默认为空"></el-input>
      </el-form-item>
    </el-form>
    <!-- 底部区 -->
    <span slot="footer" class="dialog-footer">
      <el-button @click="addDialogVisible = false">取 消</el-button>
      <el-button type="primary" @click="createProduct">确 定</el-button></span>
  </el-dialog>
  <!-- 修改产品弹窗-->
  <el-dialog v-model="editDialogVisible" title="修改产品" width="50%">
    <!-- 内容主体区 -->
    <el-form ref="editProductFormRef" :model="editProductForm" :rules="addProductFormRules" label-width="120px">
      <el-form-item label="产品名称" prop="product_name"> <!-- prop是验证规则属性 -->
        <el-select v-model="editProductForm.product_name" disabled placeholder="editProductForm.product_name">
        </el-select>
      </el-form-item>
      <el-form-item label="产品版本" prop="product_version">
        <el-row :gutter="20">
          <el-col :span="20">
            <el-select v-model="selectedMajorVersion" placeholder="选择大版本" @change="updateProductVersion">
              <el-option v-for="majorVersion in majorVersions" :key="majorVersion" :label="majorVersion"
                         :value="majorVersion"></el-option>
            </el-select>
          </el-col>
          <el-col :span="20">
            <el-select v-model="selectedMinorVersion" placeholder="选择小版本" @change="updateProductVersion">
              <el-option v-for="minorVersion in minorVersions" :key="minorVersion" :label="minorVersion"
                         :value="minorVersion"></el-option>
            </el-select>
          </el-col>
          <el-col :span="20">
            <el-select v-model="selectedPatchVersion" placeholder="选择修订版本" @change="updateProductVersion">
              <el-option v-for="patchVersion in patchVersions" :key="patchVersion" :label="patchVersion"
                         :value="patchVersion"></el-option>
            </el-select>
          </el-col>
          <el-col :span="10">
            <span>{{ selectedMajorVersion + '.' + selectedMinorVersion + '.' + selectedPatchVersion }}</span>
          </el-col>
        </el-row>
      </el-form-item>
      <el-form-item label="产品部署方式" prop="product_install_method"> <!-- prop是验证规则属性 -->
        <el-select v-model="editProductForm.product_install_method" placeholder="editProductForm.product_install_method">
          <el-option label="Docker" value="Docker"/>
          <el-option label="Tar" value="Tar"/>
          <el-option label="Kubernetes(k8s)" value="k8s"/>
        </el-select>
      </el-form-item>
      <el-form-item label="产品备注" prop="product_notes"> <!-- prop是验证规则属性 -->
        <el-input v-model="editProductForm.product_notes" placeholder="editProductForm.product_notes"></el-input>
      </el-form-item>
    </el-form>
    <!-- 底部区 -->
    <span slot="footer" class="dialog-footer">
      <el-button @click="editDialogVisible = false">取 消</el-button>
      <el-button type="primary" @click="updatePorduct">确 定</el-button></span>
    <!-- 修改产品弹窗-->
  </el-dialog>
</template>


<script>
import {Search} from "@element-plus/icons-vue";
import axios from "axios";
import zhCn from "element-plus/lib/locale/lang/zh-cn";
import {ElDialog} from "element-plus";

export default {
  name: "PmsProjectList",
  computed: {
    zhCn() {
      return zhCn
    },
  },
  components: {Search, ElDialog},
  data() {
    return {
      //获取用户列表的参数对象
      queryInfo: {
        query: "",
        pageNum: 1, // 分页默认从第一页开始
        pageSize: 10,// 默认每页显示n条数据
      },
      productsList: [],      //用户列表
      count: 0,      //总数据
      addDialogVisible: false, //控制添加产品对话框的显示与隐藏
      editDialogVisible: false, //控制修改产品对话框的显示与隐藏
      DeleteDialogVisible: false,// 控制删除产品对话框的显示与隐藏
      //添加产品表单数据
      addProductForm: {},
      //修改产品表单数据
      editProductForm: {},
      //表单验证规则
      addProductFormRules: {
        product_name: [{required: true, message: '请选择产品名字', trigger: 'blur'}],
        product_version: [{required: true, message: '请选择产品版本', trigger: 'blur'}],
        product_install_method: [{required: false, message: '请选择产品部署方式', trigger: 'blur'}],
      },
      //版本选择
      majorVersions: Array.from({length: 10}, (_, i) => `v${i + 1}`,), // 大版本数组
      minorVersions: Array.from({length: 99}, (_, i) => `${i + 1}`), // 小版本数组
      patchVersions: Array.from({length: 99}, (_, i) => `${i + 1}`), // 修订版本数组
      selectedMajorVersion: '', // 选中的大版本
      selectedMinorVersion: '', // 选中的小版本
      selectedPatchVersion: '', // 选中的修订版本
    }
  },
  created() {
    this.getProductsList();
  },
  methods: {
    //对话框打开
    openAddDialog() {
      this.addDialogVisible = true;
    },
    // 展示删除用户对话框
    showDeleteDialog(id) {
      this.$confirm('确认删除该产品嘛？', '提示', {
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
      this.getProductsList();
    },
    // 监听 页码值 改变的事件
    handleCurrentChange(newPage) {
      this.queryInfo.pageNum = newPage
      this.getProductsList()
    },
    // 更新产品版本
    updateProductVersion() {
      const product_version = `${this.selectedMajorVersion}.${this.selectedMinorVersion}.${this.selectedPatchVersion}`;
      this.addProductForm.product_version = product_version;
    },
    //删除产品
    delete_product(id) {
      try {
        axios.delete(`/products/delete/${id}`)
            .then(response => {
              const res = response.data;
              if (res.code === 0) {
                this.$message.success('删除产品成功');
                this.getProductsList(); // 刷新产品列表
              } else {
                this.$message.error(res.msg || '删除产品失败');
              }
            })
            .catch(error => {
              console.error(error);
              this.$message.error('删除产品失败');
            });
      } catch (error) {
        console.error(error);
        this.$message.error('删除用户失败');
      }
    },
    //查询所有产品 搜索产品
    async getProductsList() {
      if (this.queryInfo.query !== "") {
        //console.log(this.queryInfo.query)
        try {
          const {data: res} = await axios.get(`products/search?product_name=${this.queryInfo.query}`);
          if (res.code !== 0) {
            return this.$message.error('查询失败，没有此产品')
          }
          //console.log(res)
          this.productsList = res.products
        } catch (error) {
          return this.$message.error('查询失败，没有此产品')
        }
      } else {
        try {
          const {data: res} = await axios.get(`/products/list?pageNum=${this.queryInfo.pageNum}&pageSize=${this.queryInfo.pageSize}`);
          if (res.code !== 0) {
            return this.$message.error('获取产品列表失败')
          }
          //console.log(res)
          this.productsList = res.products
          this.count = res.pagination.count
          //console.log(this.productsList)
        } catch (error) {
          return this.$message.error('获取产品列表失败')
        }
      }
    },
    //创建产品
    async createProduct() {
      const product_version = `${this.selectedMajorVersion}.${this.selectedMinorVersion}.${this.selectedPatchVersion}`;
      await this.$refs.addProductFormRef.validate(); // 表单验证
      const formData = new FormData();
      formData.append('product_name', this.addProductForm.product_name);
      formData.append('product_version', product_version);
      formData.append('product_install_method', this.addProductForm.product_install_method);
      formData.append('product_notes', this.addProductForm.product_notes);
      const {data: res} = await axios.post("/products/create", formData, {
        headers: {
          'Content-Type': 'multipart/form-data' // 设置请求的 Content-Type
        }
      }); // 发送创建用户的请求
      if (res.code !== 0) {
        this.$message.error(res.message || "创建产品失败");
        return;
      }
      this.$message.success("创建产品成功");
      this.addDialogVisible = false; // 关闭对话框
      this.$refs.addProductFormRef.resetFields(); // 重置表单
      this.addProductForm = {};
      // 重置版本选择
      this.selectedMajorVersion = "";
      this.selectedMinorVersion = "";
      this.selectedPatchVersion = "";
      this.getProductsList(); // 刷新产品列表
    },
    //展示编辑产品的对话框
    async showEditDialog(id) {
      try {
        const response = await axios.get(`/products/search?id=${id}`);
        const res = response.data;
        //console.log(res)
        if (res && res.code === 0 && res.products && res.products.length > 0) {
          this.editDialogVisible = true;
          //console.log(this.editDialogVisible)
          this.editProductForm = res.products[0];
          // 获取已有版本信息
          const version = this.editProductForm.product_version;
          const versionsArr = version.split('.');
          this.selectedMajorVersion = versionsArr[0];
          this.selectedMinorVersion = versionsArr[1];
          this.selectedPatchVersion = versionsArr[2];
        } else {
          this.$message.error('未找到产品信息');
        }
      } catch (error) {
        console.error(error);
        this.$message.error('获取产品信息失败');
      }
    },
    //更新产品
    async updatePorduct() {
      try {
        await this.$refs.editProductFormRef.validate(); // 表单验证
        const product_version = `${this.selectedMajorVersion}.${this.selectedMinorVersion}.${this.selectedPatchVersion}`;
        console.log(product_version)
        const formData = new FormData();
        formData.append('product_name', this.editProductForm.product_name);
        formData.append('product_version', product_version);
        formData.append('product_install_method', this.editProductForm.product_install_method);
        formData.append('product_notes', this.editProductForm.product_notes);
        const {data: res} = await axios.put(`products/update/${this.editProductForm.id}`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data' // 设置请求的 Content-Type
          }
        }); // 发送创建用户的请求
        if (res.code !== 0) {
          this.$message.error(res.message || "更新用户失败");
          return;
        }
        this.$message.success("更新产品成功");
        this.editDialogVisible = false; // 关闭对话框
        this.$refs.editProductFormRef.resetFields(); // 重置表单
        this.getProductsList(); // 刷新产品列表
      } catch (error) {
        this.$message.error("表单验证失败，请检查输入");
      }
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
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.15) !important;
}

.search-area {
  margin-bottom: 20px;
}

</style>