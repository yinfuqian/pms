<template>
  <div>
    <div class="chart" ref="echart"></div>
    <hr />
    <div class="chart-container">
      <div class="chart" ref="productChart"></div>
      <div class="chart" ref="piechart"></div>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import {onMounted, ref} from 'vue';
import axios from 'axios'; // 导入 Axios 库
export default {
  setup() {
    const echart = ref(null);
    const piechart = ref(null); // 饼状图容器的引用
    const productChart = ref(null);
    const echartInit = async () => {
      const myChart = echarts.init(echart.value);
      const pieChart = echarts.init(piechart.value); // 初始化饼状图
      const productBarChart = echarts.init(productChart.value);

      // 在饼状图初始化之后，尝试调用resize
      myChart.resize({width: 800, height: 200});
      pieChart.resize({width: 400, height: 400});
      productBarChart.resize({width: 600, height: 400});
      try {
        // 从接口获取主线和定制化数据
        const mainProjectResponse = await axios.get('/mainProjects/list');
        const customerResponse = await axios.get('/customerProjects/list');
        const getPmUser = await axios.get('/user/pms');
        const getTmUser = await axios.get('/user/tms');
        const getBot = await axios.get('/products/search?product_name=bot');
        const getCall = await axios.get('/products/search?product_name=call');
        const getSee = await axios.get('/products/search?product_name=see');
        const getPal = await axios.get('/products/search?product_name=pal');
        const getLearn = await axios.get('/products/search?product_name=learn');
        //获取产品
        const bots = getBot.data;
        const calls = getCall.data;
        const sees = getSee.data;
        const pals = getPal.data;
        const learns = getLearn.data;
        console.log(bots)
        //长度
        const botValue = bots.products.length;
        const callValue = calls.products.length;
        const seeValue = sees.products.length;
        const palValue = pals.products.length;
        const learnValue = learns.products.length;
        // 产品柱状图的数据
        const productData = [botValue, callValue, seeValue, palValue, learnValue];
        //获取用户
        const pmUsers = getPmUser.data;
        const tmUsers = getTmUser.data;
        const pmValue = pmUsers.users.length; // 计算长度
        const tmValue = tmUsers.users.length; // 计算长度
        // 提取主线和定制化的数据
        const mainProjectData = mainProjectResponse.data;
        const customerData = customerResponse.data;
        const mainProjectValue = mainProjectData.projects.length; // 计算长度
        const customerValue = customerData.projects.length; // 计算长度
        const totalValue = mainProjectValue + customerValue;
        // 指定柱状图图表配置
        const option = {
          legend: {
            data: ['主线', '定制化'], // 图例的名称
            bottom: 10, // 图例距离底部的距离
          },
          title: {
            text: '项目数量总览', // 图形标题
            left: 'center', // 标题居中
          },
          xAxis: {
            type: 'value',
            max: totalValue, // 设置X轴最大值
          },
          yAxis: {
            type: 'category',
            // data: ['主线', '定制化'], // Y 轴数据为"主线"和"定制化"
            //inverse: true, // Y 轴反向，使"主线"在上方，"定制化"在下方
          },
          series: [
            {
              name: '主线',
              type: 'bar',
              data: [mainProjectValue], // 主线的数据
              itemStyle: {
                color: '#3a4848', // 主线
              },
              label: {
                show: true, // 显示标签
                position: 'right', // 标签位置，显示在柱子右侧
                offset: [5, 0], // 标签的偏移量，可以根据需要调整
                formatter: '{c}', // 标签内容为数据值
              },
              barWidth: 40, // 调整柱状图宽度
            },
            {
              name: '定制化',
              type: 'bar',
              data: [customerValue], // 定制化的数据
              itemStyle: {
                color: '#909083', // 定制化
              },
              label: {
                show: true, // 显示标签
                position: 'right', // 标签位置，显示在柱子右侧
                offset: [5, 0], // 标签的偏移量，可以根据需要调整
                formatter: '{c}', // 标签内容为数据值
              },
              barWidth: 40, // 调整柱状图宽度
            },

          ],
        };
        // 饼状图的配置
        const pieOption = {
          title: {
            text: '用户人数总览',
            left: 'center',
          },
          legend: {
            data: ['总数', 'TM', 'PM'], // 图例的名称
            bottom: 10,
          },
          series: [
            {
              name: '饼状图',
              type: 'pie',
              data: [
                {value: pmValue, name: 'PM'},
                {value: tmValue, name: 'TM'},
                {value: pmValue + tmValue, name: '总数'}
              ],
              label: {
                position: 'inside',
                fontSize: 10,
                show: true,
                formatter: '{b}: {c}', // 显示名称、数值
              },
            },
          ],
        };
        // 设置产品柱状图配置
        const productOption = {
          // 配置...
          title: {
            text: '产品版本数量概览',
            left: 'center',
          },
          xAxis: {
            type: 'category',
            data: ['bot', 'call', 'see', 'pal', 'learn'], // X 轴数据为版本名称
          },
          yAxis: {
            type: 'value',
            name: '版本数量', // Y 轴名称
          },
          series: [
            {
              name: '版本数量',
              type: 'bar',
              data: productData, // 版本数量数据
              itemStyle: {
                color: '#3a4848',
              },
              label: {
                show: true,
                position: 'top', // 标签显示在柱子的顶部
                formatter: '{c}', // 标签内容为数据值
              },
              barWidth: 40,
            },
          ],
        };

        const gridOption = {
          width: '50%', // 控制每个图表的宽度
          top: 0, // 控制图表的位置
          bottom: 0,
          left: 0,
          right: 0,
        };
        // 控制产品柱状图的位置
        const productGridOption = {
          width: '50%', // 控制产品柱状图的宽度
          top: 0, // 控制图表的位置
          bottom: 0,
          left: '50%', // 控制产品柱状图的位置
          right: 0,
        };
        // 设置图配置
        myChart.setOption(option);
        pieChart.setOption(pieOption, gridOption);
        productBarChart.setOption(productOption, productGridOption);
      } catch (error) {
        console.error('获取数据时出错：', error);
      }
    };

    // 挂载
    onMounted(() => {
      setTimeout(() => {
        echartInit();
      }, 1000); // 延迟1秒后再初始化图表
      setInterval(echartInit, 10000); // 每10秒调用 echartInit 函数刷新图表
    });
    return {
      echart,
      piechart,
      productChart,
    };
  },
};
</script>

<style scoped>
.chart-container {
  display: flex; /* 使用flex布局 */
  justify-content: space-between; /* 在容器内水平对齐，两侧留有空白空间 */
}

.chart {
  margin-bottom: 20px; /* 下边距 */
}
</style>