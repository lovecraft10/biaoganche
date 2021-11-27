<template>
  <section>
    <div style="margin-bottom: 20px;">
      <el-input v-model="input" placeholder="请输入vin号" size="medium"></el-input>
      <el-button size="big" @click="addTab()">
       绘制热力图
      </el-button>
    </div>
    <el-tabs v-model="editableTabsValue" type="card" closable @tab-remove="removeTab">
<!--      <el-tab-pane-->
<!--        v-for="(item, index) in editableTabs"-->
<!--        :key="item.name"-->
<!--        :label="item.title"-->
<!--        :name="item.name"-->
<!--      >-->
<!--      </el-tab-pane>-->
      <el-table-filter-panel v-html="html">
<!--        {{ html }}-->
      </el-table-filter-panel>
    </el-tabs>
  </section>
<!--    <div><span v-html="html">{{ html }}</span></div>-->



</template>

<script>

import {getCarMap} from "../../api/api";

export default {
  name: "carMap",
  data() {
    return{
      editableTabsValue: '1',
      editableTabs: [{
          title: '',
          name: '',
          html: ""
        }
        ],
        tabIndex: '1'
    }
  },
  methods: {
    // 增加标签页
    addTab() {
        let newTabName = ++this.tabIndex + '';
        getCarMap().then(res =>{
        this.html = res.data;
        });
        this.editableTabs.push({
          title: 'New Tab',
          name: newTabName,
          html: ""
        });

        this.editableTabsValue = newTabName;
      },
    removeTab(targetName) {
      let tabs = this.editableTabs;
      let activeName = this.editableTabsValue;
      if (activeName === targetName) {
        tabs.forEach((tab, index) => {
          if (tab.name === targetName) {
            let nextTab = tabs[index + 1] || tabs[index - 1];
            if (nextTab) {
              activeName = nextTab.name;
            }
          }
        });
      }
      this.editableTabsValue = activeName;
      this.editableTabs = tabs.filter(tab => tab.name !== targetName);
    }
    // CarMap(){
    //   getCarMap().then(res =>{
    //     this.html = res.data;
    //   })
    // }
  },
  mounted() {
    this.addTab()
  }
}
</script>

<style scoped>

</style>