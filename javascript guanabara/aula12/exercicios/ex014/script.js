function carregar(){
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    msg.innerHTML = `Agora são ${hora} horas.`
    if (hora > 0 && hora < 12){
        msg.innerHTML += ` Bom dia`
        img.src = 'manha.png'
        document.body.style.background = '#d7d7d5'
    }
    else if (hora > 12 && hora < 19){
        msg.innerHTML =+ ` Boa tarde.`
        img.src = 'tarde.png'
        document.body.style.background = '#80814e'
    }
    else{
        msg.innerHTML =+ ` Boa noite.`
        img.src = 'noite.png'
        document.body.style.background = '#1a305e'
    }
}