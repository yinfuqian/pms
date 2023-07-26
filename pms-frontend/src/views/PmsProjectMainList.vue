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
      <el-row :gutter="15">
        <!--        指定每个栏位为20-->
        <el-col :span="15">
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
    <el-table :data="productsList" border stripe>
      <el-table-column type="index"></el-table-column>
      <el-table-column label="项目名称" prop="product_name"></el-table-column>
      <el-table-column label="所属区域" prop="product_version"></el-table-column>
      <el-table-column label="项目编号" prop="product_install_method"></el-table-column>
      <el-table-column label="所属PM" prop="product_notes"></el-table-column>
      <el-table-column label="驻场TM" prop="product_notes"></el-table-column>
      <el-table-column label="部署产品" prop="product_notes"></el-table-column>
      <el-table-column label="更新日期" prop="product_notes"></el-table-column>
      <el-table-column label="操作人" prop="product_notes"></el-table-column>
      <el-table-column label="更新文档" prop="product_notes"></el-table-column>
      <el-table-column label="IVC类型" prop="product_notes"></el-table-column>
      <el-table-column label="数据库类型" prop="product_notes"></el-table-column>
      <el-table-column label="中间件类型" prop="product_notes"></el-table-column>
      <el-table-column label="操作" width="100px">
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
      //获取项目列表的参数对象
      queryInfo: {
        query: "",
        pageNum: 1, // 分页默认从第一页开始
        pageSize: 10,// 默认每页显示n条数据
      },
      projectsList: [],      //项目列表
      count: 0,      //总数据
      addDialogVisible: false, //控制添加项目对话框的显示与隐藏
      editDialogVisible: false, //控制修改项目对话框的显示与隐藏
      DeleteDialogVisible: false,// 控制删除项目对话框的显示与隐藏
      //表单验证规则
      addProductFormRules: {
        product_name: [{required: true, message: '请选择项目名字', trigger: 'blur'}],
        product_version: [{required: true, message: '请选择项目版本', trigger: 'blur'}],
        product_install_method: [{required: false, message: '请选择项目部署方式', trigger: 'blur'}],
      },
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
      this.getProductsList();
    },
    // 监听 页码值 改变的事件
    handleCurrentChange(newPage) {
      this.queryInfo.pageNum = newPage
      this.getProductsList()
    },
    //查询所有项目 搜索项目
    async getProjectsList() {
      if (this.queryInfo.query !== "") {
        //console.log(this.queryInfo.query)
        try {
          const {data: res} = await axios.get(`projects/search?product_name=${this.queryInfo.query}`);
          if (res.code !== 0) {
            return this.$message.error('查询失败，没有此项目')
          }
          //console.log(res)
          this.productsList = res.products
        } catch (error) {
          return this.$message.error('查询失败，没有此项目')
        }
      } else {
        try {
          const {data: res} = await axios.get(`/mainProjects/list?pageNum=${this.queryInfo.pageNum}&pageSize=${this.queryInfo.pageSize}`);
          if (res.code !== 0) {
            return this.$message.error('获取项目列表失败')
          }
          console.log(res)
          this.productsList = res.products
          this.count = res.pagination.count
          console.log(this.productsList)
        } catch (error) {
          return this.$message.error('获取项目列表失败')
        }
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