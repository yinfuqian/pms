<template>
  <!-- 面包屑导航 -->
  <el-breadcrumb separator-class="el-icon-arrow-right">
    <el-breadcrumb-item :to="'/home'">首页</el-breadcrumb-item>
    <el-breadcrumb-item>操作历史</el-breadcrumb-item>
  </el-breadcrumb>

  <el-card>
    <!-- 搜索与添加区域 -->
    <div class="search-area">
      <el-row :gutter="20">
        <!--        指定每个栏位为20-->
        <el-col :span="20">
          <el-input v-model='queryInfo.query' clearable placeholder="输入查询（支持用户/操作）" @clear="getoperationList">
            <template #append>
              <el-button slot="append" @click="getoperationList">
                <el-icon>
                  <Search/>
                </el-icon>
              </el-button>
            </template>
          </el-input>
        </el-col>
      </el-row>
    </div>
    <!--      操作日志列表区域-->
    <el-table :data="operationList" border stripe>
      <el-table-column type="index"></el-table-column>
      <el-table-column label="时间" prop="timestamp" width="200"></el-table-column>
      <el-table-column label="用户" prop="user" width="100"></el-table-column>
      <el-table-column label="操作" prop="formatted_content" width="700"></el-table-column>
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
  name: "pmsOperationList",
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
      operationList: [],      //日志列表
      count: 0,      //总数据


    }
  },
  created() {
    this.getoperationList();
  },
  methods: {
    // 监听 page size 改变的事件
    handleSizeChange(newSize) {
      this.queryInfo.pageSize = newSize //重新知道每页数量
      this.getoperationList();
    },
    // 监听 页码值 改变的事件
    handleCurrentChange(newPage) {
      this.queryInfo.pageNum = newPage
      this.getoperationList()
    },
    //查询所有操作日志 搜索操作日志
    async getoperationList() {
      if (this.queryInfo.query !== "") {
        //console.log(this.queryInfo.query)
        try {
          const {data: res} = await axios.get(`history/search?search_query=${this.queryInfo.query}`);
          if (res.code !== 0) {
            return this.$message.error('查询失败，没有此操作日志')
          }
          //console.log(res)
          this.operationList = res.operations
        } catch (error) {
          return this.$message.error('查询失败，没有此操作日志')
        }
      } else {
        try {
          const {data: res} = await axios.get(`/history/list?pageNum=${this.queryInfo.pageNum}&pageSize=${this.queryInfo.pageSize}`);
          if (res.code !== 0) {
            return this.$message.error('获取操作日志列表失败')
          }
          //console.log(res)
          this.operationList = res.operations
          //console.log(this.operationList)
          this.count = res.pagination.count
          //console.log(this.operationList)
        } catch (error) {
          return this.$message.error('获取操作日志列表失败')
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