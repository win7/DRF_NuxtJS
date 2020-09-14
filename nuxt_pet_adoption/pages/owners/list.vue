<template>
	<div>
		<!-- <span> {{ welcome }}</span> -->
		<table class="table table-striped">
			<thead>
				<tr>
					<th scope="col">#</th>
					<th scope="col"> Nombres </th>
					<th scope="col"> Apellidos </th>
					<th scope="col"> Teléfono </th>
					<th scope="col"> Dirección </th>	
				</tr>
			</thead>
			<tbody>
				<tr v-for="(item, index) in owners">
					<th scope="row"> {{ index + 1 }} </th>
					<td> {{ item.first_name }} </td>
					<td> {{ item.last_name }} </td>
					<td> {{ item.phone }} </td>
					<td> {{ item.address }} </td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script>
	export default {
		name: "List",
		layout: "default",
		components: {
			
		},
		data () {
			return {
				welcome: "List",
				owners: []
			}
		},
		methods: {
			async list() {
				try {
					let response = await this.$axios.get("/api/owners/");
					console.log(response);

					if (response.status === 200) {
						this.owners = response.data;
					}
				} catch (error) {
					console.log(error.response);
				}
			},
		},
		computed: {
			
		},
		filters: {
			
		},
		beforeCreate () {
			console.log("1 - List beforeCreate");
		},
		created () {
			console.log("2 - List created");
		},
		beforeMount () {
			console.log("3 - List beforeMount");
		},
		mounted () {
			console.log("4 - List mounted");

			this.list();
		},
		beforeUpdate () {
			console.log("5 - List beforeUpdate");
		},
		updated () {
			console.log("6 - List updated");
		},
		beforeDestroy () {
			console.log("7 - List beforeDestroy");
		},
		destroyed () {
			console.log("8 - List destroyed");
		}
	}
</script>

<style>

</style>