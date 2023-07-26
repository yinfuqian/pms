<template>
  <div class="common-layout">
    <el-container>
      <!--      侧边-->
      <el-aside width="200px">
        <el-menu>
          <template v-for="item in items">
            <el-sub-menu v-if="item.subItems && item.subItems.length>0" :key="item.id" :index="item.path || ''">
              <template #title>
                <component :is="item.icon" style="width: 18px;height: 18px"></component>
                <span>&nbsp;&nbsp;&nbsp;&nbsp;{{ item.title }}</span>
              </template>
              <el-menu-item v-for="subItem in item.subItems" :key="subItem.id" :index="subItem.path || ''"
                            @click="handleMenuClick(subItem.path)" style="background-color: #b1b6d5">
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
            <img src="@/static/logo.png" class="logo" alt="logo" height="50px" style="margin-left: -20px;">
            <span>PMS项目管理系统</span>
            <el-button type="warning" @click="logout" style="margin-left: 710px">退出</el-button>
          </div>
        </el-header>
        <!--        主体-->
        <el-main>
          <router-view></router-view>
        </el-main>
        <el-footer  style="background-color: slategrey;height: 30px" ></el-footer>
      </el-container>
    </el-container>
  </div>
</template>
<script>
import {ElImage, ElMenu} from "element-plus";
import {Coin, HomeFilled, House, Location, Monitor, User} from "@element-plus/icons-vue";
import {shallowRef} from "vue";

export default {
  name: "PmsHome",
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
            path: "project_customer",
            title: "定制化",
            icon: Coin
          }],
      },
      {
        id: 3,
        path: "user_list",
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
  }
  ,
  methods: {
    logout() {
      window.sessionStorage.clear();
      this.$router.push('/login')
    }
    ,
    handleMenuClick(path) {
      if (path) {
        this.$router.push(path)
      }
    },
  }
  ,

}
</script>
<style lang="less" scoped>
.common-layout{
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
