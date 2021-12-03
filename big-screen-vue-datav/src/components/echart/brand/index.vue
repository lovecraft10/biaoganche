<!--<template>-->
<!--  <div>-->
<!--    <Chart :cdata="ranking" />-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import Chart from './chart.vue';-->
<!--import {GETBRAND} from "../../../api/api";-->
<!--export default {-->
<!--  data () {-->
<!--    return {-->
<!--      ranking: {-->
<!--          data: [-->
<!--            {-->
<!--              name: '',-->
<!--              value: 55-->
<!--            },-->
<!--            {-->
<!--              name: '',-->
<!--              value: 120-->
<!--            },-->
<!--            {-->
<!--              name: '',-->
<!--              value: 78-->
<!--            },-->
<!--            {-->
<!--              name: '',-->
<!--              value: 66-->
<!--            },-->
<!--            {-->
<!--              name: '',-->
<!--              value: 80-->
<!--            },-->
<!--            {-->
<!--              name: '',-->
<!--              value: 80-->
<!--            },-->
<!--            {-->
<!--              name: '',-->
<!--              value: 80-->
<!--            },-->
<!--            {-->
<!--              name: '',-->
<!--              value: 80-->
<!--            },-->
<!--            {-->
<!--              name: '',-->
<!--              value: 80-->
<!--            },-->
<!--            {-->
<!--              name: '',-->
<!--              value: 80-->
<!--            }-->
<!--          ],-->
<!--        }-->
<!--    }-->
<!--  },-->
<!--  components: {-->
<!--    Chart,-->
<!--  },-->
<!--  mounted () {-->
<!--    this.getBrand()-->
<!--  },-->
<!--  methods: {-->
<!--    getBrand() {-->
<!--      GETBRAND().then(res => {-->
<!--        let yearRes = []-->
<!--        let yearFrame = res.info-->
<!--        for (var i = 0; i<yearFrame.length; i++) {-->
<!--          var seriesItem = {-->
<!--            value: null,-->
<!--            name: ""-->
<!--          }-->
<!--          seriesItem.name = yearFrame[i].brand-->
<!--          seriesItem.value = yearFrame[i].nums-->
<!--          yearRes.push(seriesItem)-->
<!--        }-->
<!--        this.cdata.ranking.data = yearRes-->
<!--      });-->
<!--    }-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<style lang="scss" scoped>-->
<!--</style>-->
