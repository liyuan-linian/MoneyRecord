<template>
    <el-form :model="mqttM" label-width="100px"><el-button type="primary" @click="onSubmit()">提交</el-button></el-form>
</template>

<script lang="ts" setup>
import { ref , reactive } from 'vue'
import axios from 'axios'
const FPath0 = 'http://localhost:5000/test/post'
const FPath1 = 'http://localhost:5000/test/get'

const mqttM = reactive({
    num1:'123',
    num2:'456',
    num3:'789',
})
const onSubmit = () => {
    axios.post(FPath0, mqttM).then(res => {
    console.log(res.data.name)
})
}
</script>