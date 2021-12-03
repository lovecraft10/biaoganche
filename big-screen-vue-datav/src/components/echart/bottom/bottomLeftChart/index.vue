<template>
  <div>
    <Chart :cdata="cdata" />
  </div>
</template>
<!--'0~20w', '20~40w', '40~60w', '60~80w', '80~100w','>100w'-->
<!--116, 74, 19, 8, 4, 9-->
<script>
import Chart from './chart.vue'
import {GETMONEY} from "../../../../api/api";
export default {
  data () {
    return {
      cdata: {
        moneyData: [],
        numData: [],
        rateData:[]
      }
    }
  },
  components: {
    Chart,
  },
  mounted () {
    // this.setData()
    this.getMoney()
  },
  methods: {
    // 根据自己的业务情况修改
    // setData () {
    //   for (let i = 0; i < this.cdata.numData.length; i++) {
    //     let rate = this.cdata.numData[i] / 230;
    //     this.cdata.rateData.push(rate.toFixed(2));
    //   }
    // },
    getMoney() {
      GETMONEY().then(res => {
        this.cdata.moneyData = res.money
        this.cdata.numData = res.nums
        this.cdata.rateData = res.rate
      });
    }
  }
};
</script>

<style lang="scss" scoped>
</style>
