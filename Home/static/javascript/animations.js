function faqAnimate() {
    let faq_pregunta = $('.faq-pregunta');
    faq_pregunta.each(function () {
        $(this).on('click', function () {
            $(this).next('.faq-respuesta').slideToggle('slow');
            let i = $(this).find('i');
            if (i.hasClass('rotarAbajo')) {
                i.addClass('rotarArriba').removeClass('rotarAbajo');
            } else {
                i.addClass('rotarAbajo').removeClass('rotarArriba');
            }
        });
    });
};

function animateDevices() {
    let devices = $('.dispositivo');
    let device = devices[0];
    let firstDevice = $('.lista-dispositivo > div:first');
    let notFirstDevice = $('.lista-dispositivo > div:not(:first)');
    let listDevice = $('.lista-dispositivo');
    $(notFirstDevice).css('display', 'none');
    $(firstDevice).css('display', 'block');
    $(device).addClass('aparecerIzquierda');
    setTimeout(() => {
        $(device).removeClass('aparecerIzquierda').addClass('desaparecerIzquierda');
    }, 3000);
    $(firstDevice).appendTo(listDevice);
}

function menuMovil() {

    /*Menú móvil*/
    let btn_menu = $('.btn-menu');
    let menu = $('header > nav')[0];
    $(btn_menu).click(function (e) {
        $(menu).slideToggle('slow');
        e.preventDefault();
    });
    $(window).resize(function () {
        if ($(window).width() > 758) {
            $(menu).show();
        } else {
            $(menu).hide();
        }
    });
}

function slideSubMenu() {
    let has_submenu = $('.has-submenu');
    let submenu = $('.submenu');
    let mediaQuery = window.matchMedia('(min-width: 798px)');
    console.log(mediaQuery.matches);
    if (mediaQuery.matches) {
        $(has_submenu).hover(function () {
            // over
            $(submenu).stop().slideDown(200);
        }, function () {
            // out
            $(submenu).stop().slideUp(200);
        }
        );
        $(has_submenu).off('click');
    } else {
        $(has_submenu).click(function (e) {
            e.preventDefault();
            $(submenu).stop().slideToggle(200);
        });
        $(has_submenu).off('hover');
    }

}

