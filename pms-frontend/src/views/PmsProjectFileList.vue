<template>
  <div class="common-layout">
    <el-container>
      <!--      侧边-->
      <el-aside width="170px">
        <el-menu>
          <template v-for="item in items">
            <el-sub-menu v-if="item.subItems && item.subItems.length>0" :key="item.id" :index="item.path || ''">
              <template #title>
                <component :is="item.icon" style="width: 18px;height: 18px"></component>
                <span>&nbsp;&nbsp;&nbsp;&nbsp;{{ item.title }}</span>
              </template>
              <el-menu-item v-for="subItem in item.subItems" :key="subItem.id" :index="subItem.path || ''"
                            style="background-color: #b1b6d5" @click="handleMenuClick(subItem.path)">
                <component :is="subItem.icon" style="width: 18px;height: 18px"></component>
                <span>&nbsp;&nbsp;&nbsp;&nbsp;{{ subItem.title }}</span></el-menu-item>
            </el-sub-menu>
            <el-menu-item v-if="!item.subItems" :key="item.path" :index="item.path" @click="handleMenuClick(item.path)">
              <component :is="item.icon" style="width: 18px;height: 18px"></component>
              <span>&nbsp;&nbsp;&nbsp;&nbsp;{{ item.title }}</span>
            </el-menu-item>
          </template>
        </el-menu>
      </el-aside>
      <!--      头部-->
      <el-container>
        <el-header class="el-header">
          <div>
            <img alt="logo" class="logo" height="50px" src="@/static/logo.png" style="margin-left: -20px;">
            <span>PMS项目管理系统</span>
            <el-button style="margin-left: 710px" type="warning" @click="logout">退出</el-button>
          </div>
        </el-header>
        <!--        主体-->
        <el-main>
          <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="'/home'">首页</el-breadcrumb-item>
            <el-breadcrumb-item v-if="project_type === 'main'" :to="'/mainProjects'">主线</el-breadcrumb-item>
            <el-breadcrumb-item v-else :to="'/customerProjects'">定制化</el-breadcrumb-item>
            <el-breadcrumb-item :to="''">文件列表</el-breadcrumb-item>
          </el-breadcrumb>
          <!-- 文件列表 -->
          <div class="file-list"  v-if="!isLoading">
            <ul>
              <li v-for="(fileName, index) in fileList" :key="index" class="file-list-item" :class="{ 'first-item': index === 0 }">
                {{ fileName }}
                 <a :href="getDownloadLink(fileName)" target="_blank" class="download-link">
                   <el-button type="primary" icon="download">下载文件</el-button>
                 </a>
              </li>
            </ul>
            <p v-if="isFileListEmpty" style="margin-top: 60px; color: firebrick; text-align: center; font-size: 20px">文件列表为空，请先上传文件后再进行查询!!!</p>
          </div>
          <p v-else style="margin-top: 60px;color: #282828;text-align: center; font-size: 20px">加载中...</p>
        </el-main>
        <el-footer style="background-color: slategrey;height: 30px"></el-footer>
      </el-container>
    </el-container>
  </div>

</template>
<script>
import {ElImage, ElMenu} from "element-plus";
import {Coin, HomeFilled, House, Location, Monitor, User} from "@element-plus/icons-vue";
import {shallowRef} from "vue";
import axios from "axios";

export default {
  name: "PmsProjectFileList",
  components: {
    Monitor,
    User,
    House,
    HomeFilled,
    Location,
    ElImage,
    ElMenu,
  },
  setup() {
    const items = shallowRef([
      {
        id: 1,
        path: "home",
        title: "首页",
        icon: HomeFilled,
      },
      {
        id: 2,
        title: "项目管理",
        icon: House,
        subItems: [
          {
            id: 21,
            path: "mainProjects",
            title: "主线",
            icon: Coin
          },
          {
            id: 22,
            path: "customerProjects",
            title: "定制化",
            icon: Coin
          }],
      },
      {
        id: 3,
        path: "users",
        title: "用户管理",
        icon: User,
      },
      {
        id: 4,
        path: "products",
        title: "产品管理",
        icon: Monitor,
      },
      {
        id: 5,
        path: "history",
        title: "操作历史",
        icon: Location,
      },
    ]);
    const handleMenuClick = (path) => {
      if (path) {
      }
    };
    return {
      items, handleMenuClick,
    }
  },
  props: {
    project_type: String, // 定义接受的参数类型
    project_name: String
  },
  data() {
    return {
      fileList: [], //文件列表
      isFileListEmpty: true, // 初始状态为文件列表为空
      isLoading: true, // 初始状态为加载中

    }
  },
  methods: {
    logout() {
      window.sessionStorage.clear();
      this.$router.push('/login')
    },
    handleMenuClick(path) {
      if (path) {
        this.$router.push(path)
      }
    },
    // 提取文件名中的年月日信息
    extractDateFromFileName(fileName) {
      const dateMatch = fileName.match(/(\d{8})-/); // 正则匹配年月日部分
      if (dateMatch) {
        const dateStr = dateMatch[1]; // 提取匹配到的日期字符串
        return {
          fileName,
          date: dateStr,
        };
      }
      return {
        fileName,
        date: "", // 如果无法匹配日期，则将日期设为空字符串
      };
    },
    //文件下载
    getDownloadLink(fileName) {
      return `/api/file/download?project_type=${this.project_type}&project_name=${this.project_name}&file_name=${fileName}`;
    },
  },
  created() {
    this.isLoading = true; // 开始加载
    // 请求文件列表数据
    const apiUrl = `/file/list?project_type=${this.project_type}&project_name=${this.project_name}`;
    axios
        .get(apiUrl)
        .then((response) => {
          // 处理响应数据
          const fileList = response.data.files;
          if (fileList.length > 0) {
            this.isFileListEmpty = false; // 文件列表不为空
          }
          this.fileList = fileList;
          this.isLoading = false; // 加载完成
          // 预处理文件列表，提取年月日信息
          const processedFileList = fileList.map((fileName) => this.extractDateFromFileName(fileName));
          // 对提取后的文件列表按年月日信息排序
          processedFileList.sort((a, b) => a.date.localeCompare(b.date));

          // 更新组件的文件列表
          this.fileList = processedFileList.map((item) => item.fileName);
        })
        .catch((error) => {
          console.error("请求文件列表时出错：", error);
        });
  },
}
</script>
<style lang="less" scoped>

.download-link {
  float: right; /* 靠右浮动 */
  color: black;
}
.file-list-item {
  margin-top: 20px;
  border-bottom: 1px solid #ccc; /* 添加白线分割 */
  margin-bottom: 8px; /* 添加间距 */
  padding-bottom: 8px; /* 添加底部内边距，以确保分割线下方有足够的间距 */
}

.first-item {
  margin-top: 30px; /* 第一项的上边距较大 */
}
.common-layout {
  height: 100%;
  width: 100%;
}

.el-header {
  background-color: #ffffff;
  display: flex; //设置显示为flex布局
  justify-content: space-between; //设置为flex左右布局
  padding-left: 70px; //左内边距为0（Logo贴左边）
  align-items: center; //元素上下居中（防止右边按钮贴上下边）
  color: #181818;
  font-size: 20px;

  > div { //内嵌的div样式
    display: flex;
    align-items: center; //Logo和文字上下居中
    span {
      margin-left: 11px; //文字左侧设置间距，防止与Logo紧贴
      white-space: nowrap;
    }
  }
}

.el-aside {
  background-color: #2c3e50;

  .el-menu {
    border-right: none;
  }

}

.el-main {
  background-color: cadetblue;

}

.header {
  background-color: #eaedf1;
  padding-left: 0px;
  display: flex;
  align-items: center;
}

.logo {
  height: 66px;
}

.el-container {
  height: 100%;
}

.el-menu {
  background-color: #b1b6d5;

}
</style>
