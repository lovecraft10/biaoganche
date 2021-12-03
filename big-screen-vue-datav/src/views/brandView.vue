<template>
  <div id="centerLeft1">
    <div class="bg-color-black">
      <div class="d-flex pt-2 pl-2">
        <span>
          <icon name="chart-pie" class="text-icon"></icon>
        </span>
        <div class="d-flex">
          <span class="fs-xl text mx-2">车辆品牌统计</span>
          <dv-decoration-1 class="dv-dec-1" />
        </div>
      </div>
      <div class="ranking">
        <dv-scroll-ranking-board class="dv-scr-rank-board mt-1" :config="ranking" />
      </div>
    </div>
  </div>
</template>

<script>

import {GETBRAND} from "../api/api";

export default {
  data() {
    return {
      ranking: {
        data: [
          {name: '', value: 55},
          {name: '', value: 120},
          {name: '', value: 78},
          {name: '', value: 66},
          {name: '', value: 80},
          {name: '', value: 80},
          {name: '', value: 80},
          {name: '', value: 80},
          {name: '', value: 80},
          {name: '', value: 80}
        ],
        carousel: 'single',
      }
    }
  },
  components: {
  },
  mounted() {
    this.getBrand()
  },
  methods: {
    getBrand() {
      GETBRAND().then(res => {
        let rankRes = []
        let rankFrame = res.info
        console.log(res.info[0].brand)
        for (var i = 0; i < 15; i++) {
          var dataItem = {
            name: '',
            value: []
          }
          dataItem.name = rankFrame[i].brand
          dataItem.value = rankFrame[i].nums
          rankRes.push(dataItem)
        }
        this.ranking.data = rankRes
        this.ranking = { ...this.ranking }
      });
    }
  }
};
</script>

<style lang="scss" scoped>
#centerLeft1 {
  $box-width: 200px;
  $box-height: 410px;
  padding: 16px;
  height: $box-height;
  min-width: $box-width;
  border-radius: 5px;
  .bg-color-black {
    height: $box-height - 30px;
    border-radius: 10px;
    .ranking {
      padding: 10px;
      width: 96%;
      .dv-scr-rank-board {
        height: 280px;
      }
    }
  }
  .text {
    color: #c3cbde;
  }
  .dv-dec-1 {
    position: relative;
    width: 100px;
    height: 20px;
    top: -3px;
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
