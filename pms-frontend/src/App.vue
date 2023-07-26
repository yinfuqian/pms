<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
 <div id="app" class="main">
  <router-view></router-view>
 </div>
</template>
<!--全局布局-->
<style scoped>
.main {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: -65px;
  width: 100%;
  height: 100%;
}
</style>
