<script>
	import { onMount } from 'svelte'
	var data = [];
	let text = "";
	async function getData() {
		let response = await fetch('/api/homepage').then(response => response.json());
		data = response['user'];
	}
	onMount(getData);

	async function postInput(){
		// alert('Into')
		let form = new FormData();
		form.append('name', text);
		let response = await fetch('/api/homepage', {
			method: 'POST',
			body: form
		}).then(response => response.json());
		data = response['user']
	}

</script>

<style>
	h1 {
		color: deepskyblue;
	}
</style>

<h1>List</h1>
{#await data then gotten}
	{#each gotten as element}
		<li>{element}</li>
	{/each}
{/await}

<form>
	Name: <input type="text" bind:value={text}>
</form>
<button on:click={postInput}>Add new</button>
<h2>{text}</h2>>


