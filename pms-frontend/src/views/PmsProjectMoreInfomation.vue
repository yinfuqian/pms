<template>
  <!-- 面包屑导航 -->
  <el-breadcrumb separator-class="el-icon-arrow-right">
    <el-breadcrumb-item :to="'/home'">首页</el-breadcrumb-item>
    <el-breadcrumb-item :to="''">项目管理</el-breadcrumb-item>
    <el-breadcrumb-item :to="'/mainProjects'">主线</el-breadcrumb-item>
    <el-breadcrumb-item>项目列表</el-breadcrumb-item>
  </el-breadcrumb>

</template>

<script>
export default {
  name: "PmsProjectMoreInfomation"
}
</script>

<style scoped>

</style>