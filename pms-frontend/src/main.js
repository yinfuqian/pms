import './assets/main.css'
import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import 'element-plus/dist/index.css'
import locale from 'element-plus/lib/locale/lang/zh-cn'
//icon
import * as ElIcon from '@element-plus/icons-vue'
// axios
import axios from 'axios'
//中文
import zhCn from 'element-plus/lib/locale/lang/zh-cn'

// element-ui
import ElementPlus, {
    ElAside,
    ElButton, ElConfigProvider, ElDialog,
    ElForm,
    ElFormItem,
    ElHeader,
    ElImage,
    ElInput,
    ElMain,
    ElMessage,
} from 'element-plus'



axios.defaults.baseURL = '/api';
axios.defaults.headers.post["Content-Type"] = "application/json";
//布局
const app = createApp(App)
app.provide('$axios', axios)
// axios 拦截器
axios.interceptors.request.use(config => {

    config.headers.Authorizatio = window.sessionStorage.getItem("token");
    console.log(config);

    return config;
})
//创建应用
app.use(router).use(
    ElementPlus,
    ElForm,
    ElMessage,
    ElInput,
    ElButton,
    ElFormItem,
    ElMain,
    ElHeader,
    ElAside,
    ElImage,
    ElConfigProvider,
    ElDialog,
    {locale: zhCn});

Object.keys(ElIcon).forEach(function (key) {
    app.component(ElIcon[key].name, ElIcon[key])
})

app.mount('#app')

