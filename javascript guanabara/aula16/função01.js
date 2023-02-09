let v1 = 9
let v2 = 7
let res = impapar(v1+v2)
console.log(res)

function impapar(x){
    if (x % 2 == 0){
        return 'par'
    }
    else{
        return 'impar'
    }
}