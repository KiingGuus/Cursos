var inicio000 = document.getElementById('numberini');
var fim000 = document.getElementById('numberfim');
var pulos000 = document.getElementById('numberpul');
function iniciar(){
    var res = document.getElementById('res');
    var inicio = Number(inicio000.value);
    var fim = Number(fim000.value);
    var pulos = Number(pulos000.value);
    if (inicio <= 0 || fim <= inicio || pulos <= 0 || pulos >= fim){
        res.innerHTML = ('[ERRO] Informações erradas!');
    } else{
        for( var somando = inicio; somando <= fim; somando += pulos){
            res.innerHTML += `➡ ${somando}`;
        }
    }
}
function reiniciar(){
    document.getElementById('form').reset()
    res.innerHTML = ''
}