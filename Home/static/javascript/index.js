
$(document).ready(function () {

    // Menú
    slideSubMenu();
    menuMovil();
    // Slide Imagenes
    animateDevices();
    setInterval(() => {
        animateDevices();
    }, 3800);
    // FAQ
    faqAnimate();
});
