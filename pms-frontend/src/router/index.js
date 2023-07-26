import {createRouter, createWebHistory} from "vue-router";
import PmsHome from '../views/PmsHome.vue';
import PmsUserLogin from "@/views/PmsUserLogin.vue";
import PmsHomeChart from "@/views/PmsHomeChart.vue";
import PmsUserList from "@/views/PmsUserList.vue";
import PmsHistory  from "@/views/PmsHistory.vue";
import PmsProductList from "@/views/PmsProductList.vue";
import PmsProjectMainCustomerList from "@/views/PmsProjectCustomerList.vue";
import PmsProjectMainList from "@/views/PmsProjectMainList.vue";
//自定义路由
const routes = [
    //主页
    {path: '/', redirect: '/home'},
    {
        path: '/home',
        name: 'PmsHome',
        component: PmsHome,
        redirect: '/home_chart',
        children: [{path: '/home_chart', component: PmsHomeChart}]
    },
    //项目管理  主线
    {
        path: '/mainProjects',
        name: 'PmsProjectMainList',
        component: PmsHome,
        redirect: '/mainProjects',
        children: [{path: '/mainProjects', component: PmsProjectMainList}]
    },
    //定制化
    {
        path: '/project_customer',
        name: 'PmsProjectMainCustomerList',
        component: PmsHome,
        redirect: '/project_customer',
        children: [{path: '/project_customer', component: PmsProjectMainCustomerList}]
    },
    //用户列表
    {
        path: '/users',
        name: 'PmsUserList',
        component: PmsHome,
        redirect: '/users',
        children: [{path: '/users', component: PmsUserList}]
    },
    //产品管理
     {
        path: '/products',
        name: 'PmsProductList',
        component: PmsHome,
        redirect: '/products',
        children: [{path: '/products', component: PmsProductList}]
    },
    //操作历史
     {
        path: '/history',
        name: 'PmsHistory',
        component: PmsHome,
        redirect: '/history',
        children: [{path: '/history', component: PmsHistory}]
    },
    //用户登录
    {
        path: '/login',
        name: 'UserLogin',
        component: PmsUserLogin
    }
];


const router = createRouter({
    history: createWebHistory(),
    routes
});

//挂在路由守卫
router.beforeEach((to, from, next) => {
    //如果用户在登录页面，直接放行
    if (to.path == '/login') return next();
    //从sessionStorage 里面获取token
    const tokenStr = window.sessionStorage.getItem("token");
    //没有token 强制登录，有则放行
    if (!tokenStr) return next("/login");
    next();
})

export default router;