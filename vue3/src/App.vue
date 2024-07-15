<script setup lang="ts">
import router from './router';
</script>

<template>
  <nav >
    <div class="router">
    <div style="font-weight: bold;">导航 |</div>
    <router-link to="/"> 我的数据 </router-link>  |
    <router-link to="/about"> 数据分析</router-link> |
    <router-link to="/help"> 关于帮助</router-link>
    </div>
    <div class="login">
      <router-link to="/login">登录账号</router-link> | 
      <router-link to="/register">注册账号</router-link> |
      <router-link to="/test">仅供测试</router-link>
    </div>
  </nav>

<div>
  <router-view/>
</div>

</template>

<style lang="less">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.router {

  text-align: left;
  justify-content: flex-start; 
  display: flex;
  align-items: center;
}

.login {
  flex:1;
  text-align: right;          
  justify-content: flex-end;
  display: flex;
  align-items: center;
}

nav {
  padding: 10px;
  display: flex;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
