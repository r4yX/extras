function send_color(colour) {
    const cacaImg = document.getElementById("caca")
    const heladoImg = document.getElementById("helado")
    const dineroImg = document.getElementById("dinero")
    const explosionImg = document.getElementById("explosion")
    function stopExplosion() {
        explosionImg.style.display = "none"
        explosionImg.style.animation = ""
    }

    explosionImg.style.display = "block"
    explosionImg.style.animation = "explosion 0.3s linear"
    if (colour == "0") {
        dineroImg.style.display = "none"
        heladoImg.style.display = "none"
        cacaImg.style.display = "block"
    }
    else if (colour == "1") {
        dineroImg.style.display = "none"
        cacaImg.style.display = "none"
        heladoImg.style.display = "block"
    }
    else if (colour == "2") {
        heladoImg.style.display = "none"
        cacaImg.style.display = "none"
        dineroImg.style.display = "block"
    }
    setTimeout(stopExplosion, 299)
}