<script>
	import { onMount } from 'svelte'
	var data = [];
	let text = "";
	async function getData() {
		data = await fetch('/api/').then(response => response.json());
	}
	onMount(getData);

	async function postInput(){
		// alert('Into')
		let form = new FormData();
		form.append('name', text);
		data = await fetch('/api/', {
			method: 'POST',
			body: form
		}).then(response => response.json());
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


