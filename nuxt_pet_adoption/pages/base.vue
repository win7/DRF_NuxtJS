<template>
	<div>
		<span> {{ welcome }}</span>
	</div>
</template>

<script>
	export default {
		name: "Base",
		layout: "default",
		// middleware: "authenticated",
		head: {
			bodyAttrs: {
				class: "bg-slate-800"
			},
			title: "Base"
		},
		components: {
			
		},
		data () {
			return {
				welcome: "Base"
			}
		},
		methods: {
			
		},
		computed: {
			
		},
		filters: {
			
		},
		beforeCreate () {
			console.log("1 - Base beforeCreate");
		},
		created () {
			console.log("2 - Base created");
		},
		beforeMount () {
			console.log("3 - Base beforeMount");
		},
		mounted () {
			console.log("4 - Base mounted");
		},
		beforeUpdate () {
			console.log("5 - Base beforeUpdate");
		},
		updated () {
			console.log("6 - Base updated");
		},
		beforeDestroy () {
			console.log("7 - Base beforeDestroy");
		},
		destroyed () {
			console.log("8 - Base destroyed");
		}
	}
</script>

<style>
	
</style>