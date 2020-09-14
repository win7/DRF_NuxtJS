<template>
	<div class="row justify-content-md-center">
		<!-- <span> {{ welcome }}</span> -->
		<form class="col-md-6" v-on:submit.prevent="create()">
			<div class="alert alert-danger alert-dismissible" v-if="status === 400">
				<button type="button" class="close" data-dismiss="alert" v-on:click="closeAlert()"><span>&times;</span></button>
				<span class="font-weight-semibold"> Mensaje: </span> {{ message }}.
			</div>

			<div class="form-group">
				<label> Nombres </label>
				<input type="text" class="form-control" v-model="form.first_name">
			</div>
			<div class="form-group">
				<label> Apellidos </label>
				<input type="text" class="form-control" v-model="form.last_name">
			</div>
			<div class="form-group">
				<label> Teléfono </label>
				<input type="text" class="form-control" v-model="form.phone">
			</div>
			<div class="form-group">
				<label> Dirección </label>
				<input type="text" class="form-control" v-model="form.address">
			</div>
			<button type="submit" class="btn btn-primary">Submit</button>
		</form>
	</div>
</template>

<script>
	export default {
		name: "Create",
		layout: "default",
		components: {
			
		},
		data () {
			return {
				welcome: "Create",
				form: {
					first_name: "",
					last_name: "", 
					phone: "",
					address: ""
				},
				status: -1,
				message: ""
			}
		},
		methods: {
			async create() {
				try {
					let response = await this.$axios.post("/api/owners/", this.form);
					console.log(response);

					if (response.status === 201) {
						this.$router.push("/owners/list");
					}
				} catch (error) {
					console.log(error.response);
					this.status = error.response.status;
					this.message = error.response.data;
				}
			},
		},
		computed: {
			
		},
		filters: {
			
		},
		beforeCreate () {
			console.log("1 - Create beforeCreate");
		},
		created () {
			console.log("2 - Create created");
		},
		beforeMount () {
			console.log("3 - Create beforeMount");
		},
		mounted () {
			console.log("4 - Create mounted");
		},
		beforeUpdate () {
			console.log("5 - Create beforeUpdate");
		},
		updated () {
			console.log("6 - Create updated");
		},
		beforeDestroy () {
			console.log("7 - Create beforeDestroy");
		},
		destroyed () {
			console.log("8 - Create destroyed");
		}
	}
</script>

<style>

</style>