// alert("Linked")
const URL = "https://pokeapi.co/api/v2/pokemon/"

function getPoke(event) {
    event.preventDefault()
    // console.log("function linked")
    const pokeResultDiv = document.querySelector("#pokeResult")
    const pokeName = document.querySelector("#pokeName").value
    console.log(pokeName)
    pokeResultDiv.innerHTML = "Loading....."
    fetch(URL + pokeName)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            pokeResultDiv.innerHTML = `
                <h3> Number ${data.id} ${data.name} </h3>
                <img src="${data.sprites.front_default}" alt="poke_img">
            `
            for (let type of data.types) {
                pokeResultDiv.innerHTML += `
                <p> ${type.type.name} </p>
                `
            }
        })
        .catch(err => console.log(err))
}

async function randPoke() {
    console.log("random clicked")
    const pokeResultDiv = document.querySelector("#pokeResult")
    let rand = Math.floor(Math.random() * 900)
    let response = await fetch(URL + rand)
    let data = await response.json()
    pokeResultDiv.innerHTML = `
            <h3> Number ${data.id} ${data.name} </h3>
            <img src="${data.sprites.front_default}" alt="poke_img">
        `
    for (let type of data.types) {
        pokeResultDiv.innerHTML += `
            <p> ${type.type.name} </p>
            `
    }
}