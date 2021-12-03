<template>
  <div id="bottomRight">
    <div class="bg-color-black">
      <div class="d-flex pt-2 pl-2">
        <span>
          <icon name="chart-area" class="text-icon"></icon>
        </span>
        <div class="d-flex">
          <span class="fs-xl text mx-2">车辆借用台账</span>
          <div class="decoration2">
            <dv-decoration-2 :reverse="true" style="width:5px;height:6rem;" />
          </div>
        </div>
      </div>
      <div class="d-flex jc-center body-box">
        <dv-scroll-board class="dv-scr-board" :config="config" />
      </div>
    </div>
  </div>
</template>

<script>
import {GETBOOK} from "../api/api";

export default {
  data() {
    return {
      config: {
        // begin_date: "Mon, 26 Jul 2021 00:00:00 GMT"
        // car_id: 337
        // cyy: "CYY-463"
        // depart: "混合驱动研发部"
        // end_date: "Fri, 31 Dec 2021 00:00:00 GMT"
        // give_back: 0
        // id: 1
        // mobile_phone: "13785270155"
        // operator: "付斌"
        // project_name: "车辆电池拆解、电池性能测试、采购电池及安装电池（拆）"
        header: ['开始时间', '车辆id', '借用部门', '截止日期', '是否归还', '联系电话', '操作人'],
        data: [],
        rowNum: 7, //表格行数
        headerHeight: 40,
        headerBGC: '#0f1325', //表头
        oddRowBGC: '#0f1325', //奇数行
        evenRowBGC: '#171c33', //偶数行
        columnWidth: [160,80,150,150,80],
        align: ['center'],
      },
      dialogTableVisible: false,
      totalList: []
    }
  },
  components: {},
  mounted() {
    this.getBook();
    // this.getRow();
  },
  methods: {
    // getRow(value) {
    //   // let totalList = this.totalList;
    //   // this.gridData = totalList[rowIndex]
    //   console.log(value)
    //   this.config.dialogTableVisible = true
    // },
    getBook() {
      let standingData = [];
      GETBOOK().then(res => {
        // console.log(res.info)
        let dataList = res.info
        for (var i=0; i< dataList.length; i++) {
          let item = [];
          item.push(dataList[i].begin_date)
          if (dataList[i].give_back === '1'){
            item.push("<span class='colorGrass'>" + dataList[i].car_id + "</span>")
          }else{
            item.push(dataList[i].car_id)
          }
          item.push(dataList[i].depart)
          item.push(dataList[i].end_date)
          item.push(dataList[i].give_back)
          item.push(dataList[i].mobile_phone)
          item.push(dataList[i].operator)
          standingData.push(item)
        }
        // for (let o in res.info){
        //   // console.log(o)
        //   // console.log(res.info[o])
        //   var values = Object.values(res.info[o])
        //   // console.log(values)
        //   standingData.push(values)
        // }
        // console.log(standingData)
        this.config.data = standingData;
        this.totalList = res.info;
        // this.gridData = res.info[0]
        this.config = { ...this.config}
      });
      // this.config = {
      //   header: ['开始时间', '车辆id', 'cyy', '借用部门', '截止日期', '是否归还', '联系电话', '操作人'],
      //   rowNum: 7, //表格行数
      //   headerHeight: 35,
      //   headerBGC: '#0f1325', //表头
      //   oddRowBGC: '#0f1325', //奇数行
      //   evenRowBGC: '#171c33', //偶数行
      //   index: false,
      //   columnWidth: [90],
      //   align: ['center'],
      //   data: standingData
      // }

    }

  }
}
</script>

<style lang="scss" class>
$box-height: 520px;
$box-width: 100%;
#bottomRight {
  padding: 14px 16px;
  height: $box-height;
  width: $box-width;
  border-radius: 5px;
  .bg-color-black {
    height: $box-height - 30px;
    border-radius: 10px;
  }
  .text {
    color: #c3cbde;
  }
  //下滑线动态
  .decoration2 {
    position: absolute;
    right: 0.125rem;
  }
  .body-box {
    border-radius: 10px;
    overflow: hidden;
    .dv-scr-board {
      width: 900px;
      height: 450px;
    }
  }
  .chart-box {
    margin-top: 16px;
    width: 170px;
    height: 170px;
    .active-ring-name {
      padding-top: 10px;
    }
  }
}
</style>
