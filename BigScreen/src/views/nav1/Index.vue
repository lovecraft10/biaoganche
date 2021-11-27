<template>
    <section>
      <el-row>
        <!--工具条-->
        <el-col :span="24" class="toolbar" style="padding-bottom: 0px; float: none">
          <el-form :inline="true" :model="filters">
            <el-form-item>
              <el-input v-model="filters.trip_x" placeholder="行程id"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" v-on:click="getUsers">查询</el-button>
            </el-form-item>
          </el-form>
        </el-col>
        <!-- 折线图-->
        <el-col :span="25">
          <div id="chartLine" style="width:100%; height:800px;"></div>
        </el-col>
      </el-row>
    </section>
</template>


<script>
import * as echarts from "echarts";
import {TIMEandFUEL} from "../../api/api";
export default {
  name: "Index",
  data() {
    return {
      filters: {
        trip_x: ""
      },
      currentDate: new Date(),
      chartLine: null,
      chartPie: null
    };
  },
  methods: {
    handleCurrentChange() {
      this.getUsers();
    },
    getUsers() {
        let para = {trip_x: this.filters.trip_x};
        this.chartLine = echarts.init(document.getElementById("chartLine"));
        TIMEandFUEL(para).then(res => {
          this.chartLine.showLoading();
          let {reportTime, Fuel, EngSpd, VehSpd, code} = res.data;

          if (code !== 200) {
            this.$message({
              message: "服务端发生错误",
              type: "warning"
            });
          } else {
            this.chartLine.hideLoading();
            this.chartLine.setOption({
              // visualMap: [
              //   {
              //     show: false,
              //     type: 'continuous',
              //     seriesIndex: 0
              //   },
              //   {
              //     show: false,
              //     type: 'continuous',
              //     seriesIndex: 1,
              //     dimension: 0
              //   }
              //
              // ],
              title: [
                {
                  left: 'left',
                  text: "平均油耗变化图"
                },
                {
                  top: '55%',
                  left: 'left',
                  text: '发动机转速变化图'
                }
              ],
              tooltip: {
                trigger: "axis",
                axisPointer: {
                  type: 'cross'
                }
              },
              axisPointer: {
                link: [{xAxisIndex: 'all'}],
                label: {
                  backgroundColor: '#777'
                }
              },
              legend: {
                data: ['平均油耗', '发动机转速', '车速']
              },
              toolbox: {
                show: true,
                feature: {
                  dataZoom: {
                    yAxisIndex: 'none'
                  },
                  magicType: {show: true, type: ["line", "bar"]},
                  saveAsImage: {show: true}
                }
              },
              calculable: true,
              dataZoom: [
                {
                  show: true,
                  xAxisIndex: [0, 1],
                  start: 0,
                  end: 30
                },
                {
                  type: 'inside',
                  xAxisIndex: [0, 1],
                  start: 0,
                  end: 30
                }
              ],
              xAxis: [
                {
                  type: "category",
                  data: reportTime,
                  axisTick: {
                    show: false
                  },
                  boundaryGap: false
                },
                {
                  type: "category",
                  data: reportTime,
                  gridIndex: 1,
                  axisTick: {
                    show: false
                  },
                  boundaryGap: false
                }
              ],
              yAxis: [
                {
                  type: "value",
                  axixTick: {
                    show: false
                  }
                },
                {
                  gridIndex: 1,
                }
              ],
              grid: [
                {
                  bottom: '60%',
                },
                {
                  top: '60%'
                }
              ],
              series: [
                {
                  name: '平均油耗',
                  type: 'line',
                  data: Fuel,
                  sampling: 'average'
                },
                {
                  name: '车速',
                  type: 'line',
                  data: VehSpd,
                  sampling: 'average'
                },
                {
                  name: '发动机转速',
                  type: 'line',
                  data: EngSpd,
                  sampling: 'average',
                  xAxisIndex: 1,
                  yAxisIndex: 1
                }
              ]
            });
          }
        });
      },
    // drawPieChart() {
    //   this.chartPie = echarts.init(document.getElementById("chartPie"));
    //   getdrawPieChart1().then(res => {
    //     let { value, code, total } = res.data;
    //     if (code !== 200) {
    //       this.$message({
    //         message: "服务端发生错误",
    //         type: "warning"
    //       });
    //     } else {
    //       this.chartPie.setOption({
    //         title: {
    //           text: "占比",
    //           subtext: "总数:1485903",
    //           x: "center"
    //         },
    //         tooltip: {
    //           trigger: "item",
    //           formatter: "{a} <br/>{b} : {c} ({d}%)"
    //         },
    //         legend: {
    //           orient: "vertical",
    //           left: "left",
    //           // data: ["主驾", "副驾", "右后", "左后"] // 和value一一对应
    //         },
    //         toolbox: {
    //           show: true,
    //           feature: {
    //             saveAsImage: { show: true }
    //           }
    //         },
    //         series: [
    //           {
    //             name: "占比数",
    //             type: "pie",
    //             radius: "55%",
    //             data: [
    //               { value: 866228, name: "主驾" },
    //               { value: 307212, name: "副驾" },
    //               { value: 165754, name: "右后" },
    //               { value: 146709, name: "左后" }
    //             ],
    //             itemStyle: {
    //               emphasis: {
    //                 shadowBlur: 10,
    //                 shadowOffsetX: 0,
    //                 shadowColor: "rgba(0, 0, 0, 0.5)"
    //               }
    //             }
    //           }
    //         ]
    //       });
    //     }
    //   });
    // },
    drawCharts() {
      this.getUsers();
    },
  },
  mounted: function() {
    this.drawCharts();
  },
  updated: function() {
    this.drawCharts();
  },
  beforeDestroy: function (){
    this.
    drawCharts.
    clear()
  }


};
</script>

<style>
  .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }

  .clearfix:after {
      clear: both
  }
</style>