<script>
	import { onMount } from 'svelte'
	var data = [];
	let text = "www";
	async function getData() {
		let response = await fetch('/api/homepage').then(response => response.json());
		data = response['user'];
	}
	onMount(getData);

	async function postInput(){
		let form = FormData();
		form.append('name', text);
		await fetch('/api/homepage', {
			method: 'POST',
			body: form
		});
	}

</script>

<style>
	h1 {
		color: deepskyblue;
	}
</style>


{#await data then gotten}
	{#each gotten as element}
		<li>{element}</li>
	{/each}
{/await}

<h1>List</h1>
<form>
	Name: <input type="text" bind:value={text}>
</form>
<button on:click={postInput()}>Add new!</button>
<h2>{text}</h2>>


