<template>
  <div>
    <Chart :cdata="cdata" />
  </div>
</template>

<script>
import Chart from './chart.vue';
import {GETYEAR} from "../../../../api/api";
export default {
  data () {
    return {
      cdata: {
        xData: ["data1", "data2", "data3", "data4", "data5", "data6"],
        seriesData: [
          { value: 10, name: "data1" },
          { value: 5, name: "data2" },
          { value: 15, name: "data3" },
          { value: 25, name: "data4" },
          { value: 20, name: "data5" },
          { value: 35, name: "data6" }
        ]
      }
    }
  },
  components: {
    Chart,
  },
  mounted () {
    this.getYear()
  },
  methods: {
    getYear() {
      GETYEAR().then(res => {
        this.cdata.xData = res.yearData
        console.log(res.yearData)
        console.log(res.info)
        let yearRes = []
        let yearFrame = res.info
        for (var i = 0; i<yearFrame.length; i++) {
          var seriesItem = {
            value: [],
            name: ""
          }
          seriesItem.name = yearFrame[i].yearRange
          seriesItem.value = yearFrame[i].nums
          yearRes.push(seriesItem)
        }
        this.cdata.seriesData = yearRes
      });
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
