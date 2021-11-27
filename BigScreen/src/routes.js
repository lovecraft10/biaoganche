import Login from './views/Login.vue'
import NotFound from './views/404.vue'
import Home from './views/Home.vue'
import Table from './views/nav1/Table.vue'
import Door from './views/nav1/Door.vue'
import Trip from './views/nav1/Trip.vue'
import echarts from './views/charts/echarts.vue'
import Index from './views/nav1/Index.vue'
import CarMap from './views/charts/carMap.vue'


let routes = [
    {
        path: '/login',
        component: Login,
        name: '',
        hidden: true
    },
    {
        path: '/404',
        component: NotFound,
        name: '',
        hidden: true
    },
    //{ path: '/main', component: Main },
    {
        path: '/',
        component: Home,
        name: 'Index',
        leaf: true,//只有一个节点
        iconCls: 'fa fa-id-card-o',//图标样式class
        children: [
            { path: '/Index', component: Index, name: '首页' },
        ]
    },
    {
        path: '/',
        component: Home,
        name: 'Table',
        leaf: true,//只有一个节点
        iconCls: 'fa fa-id-card-o',//图标样式class
        children: [
            { path: '/table', component: Table, name: '信息汇总' },
        ]
    },
    {
        path: '/',
        component: Home,
        name: 'Door',
        leaf: true,
        iconCls: 'fa fa-bar-chart',
        children: [
            { path: '/door', component: Door, name: '车门开关次数' }
        ]
    },
    {
        path: '/',
        component: Home,
        name: 'Trip',
        leaf: true,
        iconCls: 'fa fa-bar-chart',
        children: [
            { path: '/trip', component: Trip, name: '行程划分统计' }
        ]
    },
    {
        path: '/',
        component: Home,
        name: 'CarMap',
        leaf: true,
        iconCls: 'fa fa-bar-chart',
        children: [
            { path: '/carmap', component: CarMap, name: '行车位置地图' }
        ]
    },
    {
        path: '/',
        component: Home,
        name: 'Charts',
        leaf: true,
        iconCls: 'fa fa-bar-chart',
        children: [
            { path: '/echarts', component: echarts, name: '图表展示' }
        ]
    },
    {
        path: '*',
        hidden: true,
        redirect: { path: '/404' }
    }
];

export default routes;