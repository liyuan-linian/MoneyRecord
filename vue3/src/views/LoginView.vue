<template>
    <div class="login">
      <h2>登录</h2>
      <form @submit.prevent="handleSubmit">
        <div>
          <label for="username">用户名：</label>
          <input type="text" id="username" v-model="username" />
        </div>
        <div>
          <label for="password">密码：</label>
          <input type="password" id="password" v-model="password" />
        </div>
        <button type="submit">登录</button>
      </form>
    </div>
  </template>
  
  <script>
  import { ref } from "vue";
  import axios from "axios";
  
  export default {
    setup() {
      const username = ref("");
      const password = ref("");
  
      const handleSubmit = async () => {
        try {
          const response = await axios.post("/api/login", {
            username: username.value,
            password: password.value,
          });
          if (response.data.success) {
            alert("登录成功！");
          } else {
            alert("登录失败，请检查用户名和密码。");
          }
        } catch (error) {
          console.error(error);
        }
      };
  
      return {
        username,
        password,
        handleSubmit,
      };
    },
  };
  </script>
  