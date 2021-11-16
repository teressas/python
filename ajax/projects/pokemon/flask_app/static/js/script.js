var testBtn = document.querySelector('.test-btn')

testBtn.addEventListener("click", function(){
    fetch('/api/user/create')
    .then( response => response.json())
    .then(data => {
        console.log(data);
    })
}
)

var userForm = document.querySelector('#user-form')

userForm.addEventListener('submit',function(event){
    e.preventDefault()
    console.log('form submit');
}
)

var theForm = new FormData(userForm)

console.log("Hello 1");

fetch('api/user/create',{
    method:'POST',
    body: theForm
})
.then( response => response.json())
.then( data => {
    if (data['status'] === 200){
        console.log("yes")
        var msg = data['msg']
        firstNameErrr = document.querySelector('#first_name_error')
        firstNameErrr.innerText = msg
    }
})

var pokiForm = document.querySelector('#poki-form')
pokiForm.addEventListener('submit',function(e){
    e.preventDefault()

    let poki = document.querySelector('#poki-name').value
    fetch('https://pokeapi.co/api/v2/pokemon/${poki}')
    .then(resp => resp.json())
    .then(data => {
        var img = data['sprites']['front_default']
        var imgdiv = document.querySelector('#poki-img')
        imgdiv.innerHTML = `
        <img src="${img}" alt="">
        `
        ;
    })
    console.log(poki);
})


// console.log('You have connected...')

// document.addEventListener("DOMContentLoaded", () =>{

//     let generateBtn = document.querySelector('#generate-pokemon');
//     generateBtn.addEventListener('click', renderEverything)

//     getDeleteBtn().addEventListener('click', deleteEverything);
// })

// function renderEverything(){
//     let allPokemonContainer = document.querySelector('#poke-container')
//     allPokemonContainer.innerText = "";
//     fetchKantoPokemon();

//     getDeleteBtn().style.display = 'block'
// }

// function getDeleteBtn(){
//     return document.querySelector('#delete-btn')
// }


// function fetchKantoPokemon(){
//     fetch('https://pokeapi.co/api/v2/pokemon?limit=151')
//     .then(response => response.json())
//     .then(function(allpokemon){
//         allpokemon.results.forEach(function(pokemon){
//             fetchPokemonData(pokemon);
//         })
//     })
// }

// function fetchPokemonData(pokemon){
//     let url = pokemon.url // <--- this is saving the pokemon url to a variable to use in the fetch. 
//                                 //Example: https://pokeapi.co/api/v2/pokemon/1/"
//     fetch(url)
//     .then(response => response.json())
//     .then(function(pokeData){
//         renderPokemon(pokeData)
//     })
// }


// function renderPokemon(pokeData){
//     let allPokemonContainer = document.getElementById('poke-container');
//     let pokeContainer = document.createElement("div") //div will be used to hold the data/details for indiviual pokemon.{}
//     pokeContainer.classList.add('ui', 'card');

//     createPokeImage(pokeData.id, pokeContainer);

//     let pokeName = document.createElement('h4') 
//     pokeName.innerText = pokeData.name

//     let pokeNumber = document.createElement('p')
//     pokeNumber.innerText = `#${pokeData.id}`
   
//     let pokeTypes = document.createElement('ul') //ul list will hold the pokemon types
  

//     createTypes(pokeData.types, pokeTypes) // helper function to go through the types array and create li tags for each one

//     pokeContainer.append(pokeName, pokeNumber, pokeTypes);   //appending all details to the pokeContainer div
//     allPokemonContainer.appendChild(pokeContainer);       //appending that pokeContainer div to the main div which will                                                             hold all the pokemon cards
// }

// function createTypes(types, ul){
//     types.forEach(function(type){
//         let typeLi = document.createElement('li');
//         typeLi.innerText = type['type']['name'];
//         ul.append(typeLi)
//     })
// }

// function createPokeImage(pokeID, containerDiv){
//     let pokeImgContainer = document.createElement('div')
//     pokeImgContainer.classList.add('image')

//     let pokeImage = document.createElement('img')
//     pokeImage.srcset = `https://pokeres.bastionbot.org/images/pokemon/${pokeID}.png`

//     pokeImgContainer.append(pokeImage);
//     containerDiv.append(pokeImgContainer);
// }

// function deleteEverything(event){
//     event.target.style = 'none';
//     let allPokemonContainer = document.querySelector('#poke-container')
//     allPokemonContainer.innerText = ""

//     let generateBtn = document.createElement('button')
//     generateBtn.innerText = "Generate Pokemon"
//     generateBtn.id = 'generate-pokemon'
//     generateBtn.classList.add('ui', 'secondary', 'button')
//     generateBtn.addEventListener('click', renderEverything);

//     allPokemonContainer.append(generateBtn)
// }