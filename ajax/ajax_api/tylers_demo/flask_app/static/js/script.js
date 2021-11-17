var testBtn = document.querySelector('.test-btn')
// var testBtn2 = document.querySelector('.test-btn2')

testBtn.addEventListener("click", function(){
    fetch('https://pokeapi.co/api/v2/pokemon/ditto')
    .then( response => response.json() )
    .then( data => {
        console.log(data);
    })
})

var userForm = document.querySelector("#user-form")

userForm.addEventListener('submit', function(e){
    e.preventDefault()
    console.log('form submit');

    var theForm = new FormData(userForm)

    fetch('/api/user/create',{
        method:'POST',
        body: theForm
    })
    .then( response => response.json() )
    .then( data => {
        console.log(data)
        if (data['status'] === 200) {
            console.log("yes");
            var msg = data['msg'];
            firstNameErrr = document.querySelector('#first_name_error')
            firstNameErrr.innerText = msg
        } else if (data['status'] === 400){
            var errorsMsg = data['msg']
            
            for (const key in errorsMsg) {
                console.log(key);
                errorSpan = document.querySelector(`#${key}`)
                console.log(errorSpan);
                errorSpan.innerHTML = `<p>${errorsMsg[key]}</p>`
            }
        }

    })
    
})

var pokiForm = document.querySelector('#poki-form')
pokiForm.addEventListener('submit', function(e){
    e.preventDefault('')

let poki = document.querySelector('#poki-name').value
    fetch(`https://pokeapi.co/api/v2/pokemon/${poki}`)
    .then(resp => resp.json())
    .then(data => {
        var img = data['sprites']['front_default']
        var imgdiv = document.querySelector('#poki-img')
        imgdiv.innerHTML = `
        <img src = "${img}" alt="">
        `
    })
})

// AWAIT    

// let poki = document.querySelector('#poki-name').value
// var resp = await fetch(`https://pokeapi.co/api/v2/pokemon/${poki}`)
// var data = await resp.json()

// var img = data.sprites.front_default
// var imgdiv = document.querySelector('#poki-img')
// imgdiv.innerHTML = `
// <img src="${img} alt="">
// `

// testBtn2.addEventListener("click", ()=>{
//     console.log("btn2 was pressed");
// })