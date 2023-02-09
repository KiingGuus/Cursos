let num = document.querySelector('input#fnum')
let lista = document.querySelector('select#flista')
let res = document.querySelector('div#res')
let valores = []
function isNumero(n){
    if (Number(n) >= 1 && Number(n) <= 100){
        return true
    } else{
        return false
    }
}
function inLista(n, l){
    if (l.indexOf(Number(n)) != -1){
        return true
    } else {
        return false
    }
}
function adcionar(){
    if(isNumero(num.value) && !inLista(num.value, valores)){
        valores.push(Number(num.value))
        let item = document.createElement('option')
        item.text = `Valor ${num.value} adcionado.`
        lista.appendChild(item)
        res.innerHTML = ''
    } else{
        alert('Valor inválido ou já encontrado na lista.')
    }
    num.value = ''
    num.focus()
}
function finalizar(){
    if (valores.length == 0){
        alert('Adcione valores antes de finalizar!')
    } else{
        let tot = valores.length
        let lownum = valores[0]
        let hignum = valores[0]
        let soma = 0
        let media = 0
        for(let pos in valores){
            soma += valores[pos]
            if (valores[pos] > hignum)
                hignum = valores[pos]
            if (valores[pos] < lownum)
                lownum = valores[pos]
        }
        media = soma / tot
        res.innerHTML = ''
        res.innerHTML += `<p>Ao todo temos ${tot} números cadastrados.</p>`
        res.innerHTML += `<p>O menor número cadastrado é ${lownum}</p>`
        res.innerHTML += `<p>O maior número cadastrado é ${hignum}</p>`
        res.innerHTML += `<p>A soma de todos os números cadastrados é de ${soma}</p>`
        res.innerHTML += `<p>A media de todos os número cadastrados é de ${media}</p>`

    }
}