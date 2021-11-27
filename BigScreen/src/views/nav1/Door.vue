<template>
	<section>
		<!--工具条-->
		<el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
			<el-form :inline="true" :model="filters">
				<el-form-item>
					<el-input v-model="filters.vin" placeholder="vin号"></el-input>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" v-on:click="getUsers">查询</el-button>
				</el-form-item>
			</el-form>
		</el-col>

		<!--列表-->
		<el-table :data="doorList" highlight-current-row v-loading="listLoading" @selection-change="selsChange" style="width: 100%;">
			<el-table-column type="selection" width="55">
			</el-table-column>
			<el-table-column type="index" width="60">
			</el-table-column>
			<el-table-column prop="vin" label="vin号" width="200" sortable>
			</el-table-column>
      <el-table-column prop="driverD" label="主驾驶" width="120" sortable>
			</el-table-column>
			<el-table-column prop="passengerD" label="副驾驶" width="120" sortable>
			</el-table-column>
			<el-table-column prop="rrD" label="右后" width="120" sortable>
			</el-table-column>
			<el-table-column prop="rlD" label="左后" width="120" sortable>
			</el-table-column>
<!--			<el-table-column label="操作" width="150">-->
<!--				<template scope="scope">-->
<!--					<el-button size="small" @click="handleEdit(scope.$index, scope.row)">详情</el-button>-->
<!--					<el-button type="danger" size="small" @click="handleDel(scope.$index, scope.row)">删除</el-button>-->
<!--				</template>-->
<!--			</el-table-column>-->
		</el-table>

		<!--工具条-->
		<el-col :span="24" class="toolbar">
			<el-button type="danger" @click="batchRemove" :disabled="this.sels.length===0">批量删除</el-button>
			<el-pagination layout="prev, pager, next" @current-change="handleCurrentChange" :page-size="page_size" :total="total" style="float:right;">
			</el-pagination>
		</el-col>

<!--		&lt;!&ndash;详情界面&ndash;&gt;-->
<!--		<el-dialog title="详情" v-model="detailFormVisible" :close-on-click-modal="false">-->
<!--			<el-form :model="detailForm" label-width="80px" :rules="detailFormRules" ref="detailForm">-->
<!--        <el-form-item label="姓名" prop="name">-->
<!--							<el-input v-model="detailForm.name" auto-complete="off"></el-input>-->
<!--						</el-form-item>-->
<!--				<el-row>-->
<!--            <el-col :span="12">-->
<!--  						<el-form-item label="学院">-->
<!--							<el-input v-model="detailForm.profess"></el-input>-->
<!--						</el-form-item>-->
<!--  					</el-col>-->
<!--  					<el-col :span="12">-->
<!--  						<el-form-item label="年级">-->
<!--							<el-input v-model="detailForm.grade"></el-input>-->
<!--						</el-form-item>-->
<!--  					</el-col>-->
<!--				</el-row>-->
<!--				<el-row>-->
<!--  					<el-col :span="12">-->
<!--  						<el-form-item label="电话">-->
<!--							<el-input v-model="detailForm.phone"></el-input>-->
<!--						</el-form-item>-->
<!--  					</el-col>-->
<!--  					<el-col :span="12">-->
<!--  						<el-form-item label="邮箱">-->
<!--							<el-input v-model="detailForm.email"></el-input>-->
<!--						</el-form-item>-->
<!--  					</el-col>-->
<!--				</el-row>-->
<!--				<el-row>-->
<!--  					<el-col :span="12">-->
<!--  						<el-form-item label="组别">-->
<!--							<el-input v-model="detailForm.group"></el-input>-->
<!--						</el-form-item>-->
<!--  					</el-col>-->
<!--  					<el-col :span="12">-->
<!--  						<el-form-item label="日期">-->
<!--  							<el-date-picker type="datetime" placeholder="日期" v-model="detailForm.pub_date"></el-date-picker>-->
<!--						</el-form-item>-->
<!--  					</el-col>-->
<!--				</el-row>-->
<!--				<el-form-item label="能力期待">-->
<!--					<el-input type="textarea" v-model="detailForm.power"></el-input>-->
<!--				</el-form-item>-->
<!--			</el-form>-->
<!--			<div slot="footer" class="dialog-footer">-->
<!--				<el-button @click.native="detailFormVisible = false">返回</el-button>-->
<!--			</div>-->
<!--		</el-dialog>-->
	</section>
</template>

<script>
import util from "../../common/js/util";
import { getDoorPage, removeUser, batchRemoveUser } from "../../api/api";

export default {
  data() {
    return {
      filters: {
        vin: ""
      },
      doorList: [],
      page_size: 20,
      total: 0,
      page: 1,
      listLoading: false,
      sels: [], //列表选中列

      detailFormVisible: false, //详情界面是否显示
      editLoading: false,
      detailFormRules: {
        name: [{ required: true, message: "请输入姓名", trigger: "blur" }]
      },
      //详情界面数据
      detailForm: {
        id: 0,
        name: "",
        profess: "",
        grade: 0,
        phone: 0,
        email: "",
        group: "",
        pub_data: "",
        power: ""
      }
    };
  },
  methods: {
    handleCurrentChange(val) {
      this.page = val;
      this.getUsers();
    },
    //获取用户列表
    getUsers() {
      let para = {
        page: this.page,
        vin: this.filters.vin
      };
      this.listLoading = true;
      //NProgress.start();
      getDoorPage(para).then(res => {
        this.total = res.data.total;
        this.page_size = res.data.page_size;
        this.doorList = res.data.infos;
        this.listLoading = false;
      });
    },
    //删除
    handleDel: function(index, row) {
      this.$confirm("确认删除该用户吗?", "提示", {
        type: "warning"
      })
        .then(() => {
          this.listLoading = true;
          //NProgress.start();
          let para = { id: row.id };
          removeUser(para).then(res => {
            this.listLoading = false;
            let { msg, code } = res.data;
            if (code !== 200) {
              this.$message({
                message: msg,
                type: "warning"
              });
            } else {
              this.$message({
                message: msg,
                type: "success"
              });
            }
            this.getUsers();
          });
        })
        .catch(() => {});
    },
    //显示详情界面
    handleEdit: function(index, row) {
      this.detailFormVisible = true;
      this.detailForm = Object.assign({}, row);
    },
    selsChange: function(sels) {
      this.sels = sels;
    },
    //批量删除
    batchRemove: function() {
      var ids = this.sels.map(item => item.id).toString();
      this.$confirm("确认删除选中用户吗？", "提示", {
        type: "warning"
      })
        .then(() => {
          this.listLoading = true;
          let para = { ids: ids };
          batchRemoveUser(para).then(res => {
            this.listLoading = false;
            let { msg, code } = res.data;
            if (code !== 200) {
              this.$message({
                message: msg,
                type: "warning"
              });
            } else {
              this.$message({
                message: msg,
                type: "success"
              });
            }
            this.getUsers();
          });
        })
        .catch(() => {});
    }
  },
  mounted() {
    this.getUsers();
  }
};
</script>

<style scoped>

</style>