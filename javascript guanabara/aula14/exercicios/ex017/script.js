var numero000 = document.getElementById('number')
var res = document.getElementById('res')
function calcular(){
    var numero = Number(numero000.value);
    if(numero != Number){
        res.innerHTML = '[Erro]'
    } else{
        res.innerHTML = 't'
    }
}