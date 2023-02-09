let num = document.getElementById('tnum')
let res = document.getElementById('res')
let tab =document.getElementById('seltab')
let repete = tab.indexOf(num)
function adcionar(){
    if (num.value <= 0 || num.value >= 100 || repete == true){
        alert('[ERRO] Numero invalido')
    } else{
        let item = document.createElement('option')
        tab.appendChild(item)
    }
}

function finalizar(){
    let fim = document.getElementById('finalizar')
}