function verificar(){
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.getElementById('res')
    if (fano.value == 0 || fano.value > ano){
        window.alert('[ERRO] Verifique os dados e tente novamente!')
    } else{
         var fsex = document.getElementsByName('radsex')
         var idade = ano - fano.value
         var genero = ''
         var img = document.createElement('img')
         img.setAttribute('id', 'foto')
         if (fsex[0].checked){
            genero = 'Masculino'
            if (idade >= 0 && idade < 4){
                //bebe
                img.setAttribute('src', 'bebe-600x600.png')
            } else if (idade >= 4 && idade < 13){
                //criança
                 img.setAttribute('src', 'menino-600x600.png')
            } else if (idade >= 13 && idade < 18){
                //adolescente
                img.setAttribute('src', 'adolescente-m-600x600.png')
            } else if (idade >= 18 && idade < 35){
                //adulto
                img.setAttribute('src', 'adulto-600x600.png')
            } else if (idade >= 35 && idade < 60){
                //meia idade
                img.setAttribute('src', 'meia-idade-m-600x600.png')
            } else if (idade >= 60){
                //idoso
                img.setAttribute('src', 'idoso-600x600.png')
            }
         } else if (fsex[1].checked){
            genero = 'Feminino'
            if (idade >= 0 && idade < 4){
                //bebe
                img.setAttribute('src', 'bebe-600x600.png')
            } else if (idade >= 4 && idade < 13){
                //criança
                 img.setAttribute('src', 'menina-600x600.png')
            } else if (idade >= 13 && idade < 18){
                //adolescente
                img.setAttribute('src', 'adolescente-f-600x600.png')
            } else if (idade >= 18 && idade < 35){
                //adulto
                img.setAttribute('src', 'adulta-600x600.png')
            } else if (idade >= 35 && idade < 60){
                //meia idade
                img.setAttribute('src', 'meia-idade-f-600x600.png')
            } else if (idade >= 60){
                //idoso
                img.setAttribute('src', 'idosa-600x600.png')
            }
         }
    res.style.textAlign = 'Center'
    res.innerHTML = `Detectamos o sexo ${genero} com ${idade} anos de idade.`
    res.appendChild(img)
    }
}
function reiniciar(){
    document.getElementById('form').reset()
    res.innerHTML = 'Preencha os dados acima'
}