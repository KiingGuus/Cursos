var numero000 = document.getElementById('number')
var res = document.getElementById('res')
function calcular(){
    var contador = 0
    var numero = Number(numero000.value)
    if(numero <= 0){
        window.alert('[ERRO] Numero menor ou igual a 0')
    } else{
        res.innerHTML = ''
        while (contador < 12){
            var contador = contador + 1
            var multiplos = numero * contador
            res.innerHTML += `<br>${contador} X ${numero} = ${multiplos}`
        }
    }
}