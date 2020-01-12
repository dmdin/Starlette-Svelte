<script>
	import { onMount } from 'svelte'
	export let name;
	var data = [];

	async function getData() {
		let resp = await fetch('/api/homepage');
		data = await resp.text();
	}
	onMount(getData())

</script>

<style>
	h1 {
		color: purple;
	}
</style>

<h1>Hello {name}!</h1>
{#await data then gotten}
	<p>Got: {gotten}</p>
{/await}
