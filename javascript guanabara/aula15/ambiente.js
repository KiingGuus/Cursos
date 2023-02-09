let num = [5,8,7,2,6]
num.push(1)
num.sort()
console.log(num)
console.log(`O array tem ${num.length} posições`)
console.log(`O primeiro valor do vetor é ${num[0]}`)
let pos = num.indexOf(9)
if (pos == -1){
    console.log(`Valor nao encontrado`)
}
else{
    console.log(`O valor 8 esta na posição ${pos}`)
}
