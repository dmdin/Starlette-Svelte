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
    body {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-items: center;
    }
	h1 {
		color: deepskyblue;
        font-size: 3em;
	}
    li {
        list-style-type: none;
        font-size: 1.2em;
    }
    .form {
        display: flex;
        flex-direction: row;
    }

</style>

<body>
<h1>Tournament List</h1>

<div class="form">
    <form>
        Name: <input type="text" bind:value={text}>
    </form>
    <button on:click={postInput}>Add new</button>
</div>

<div>
{#await data then gotten}
	{#each gotten as element}
		<li>{element}</li>
	{/each}
{/await}
</div>
</body>

