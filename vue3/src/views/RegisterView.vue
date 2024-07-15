<template>
    <div class="register">
      <h2>注册</h2>
      <form @submit.prevent="handleSubmit">
        <div>
          <label for="username">用户名：</label>
          <input type="text" id="username" v-model="username" />
        </div>
        <div>
          <label for="email">邮箱：</label>
          <input type="email" id="email" v-model="email" />
        </div>
        <div>
          <label for="password">密码：</label>
          <input type="password" id="password" v-model="password" />
        </div>
        <button type="submit">注册</button>
      </form>
    </div>
  </template>
  
  <script>
  import { ref } from "vue";
  import axios from "axios";
  
  export default {
    setup() {
      const username = ref("");
      const email = ref("");
      const password = ref("");
  
      const handleSubmit = async () => {
        try {
          const response = await axios.post("/api/register", {
            username: username.value,
            email: email.value,
            password: password.value,
          });
          if (response.data.success) {
            alert("注册成功！");
          } else {
            alert("注册失败，请检查输入信息。");
          }
        } catch (error) {
          console.error(error);
        }
      };
  
      return {
        username,
        email,
        password,
        handleSubmit,
      };
    },
  };
  </script>
  