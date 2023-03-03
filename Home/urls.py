from django.urls import path
from django.conf.urls import handler404
from .views import error_404_view
from .views import Home, WebDesign, SEO, FAQ, Contacto

urlpatterns=[
    path('', Home),
    path('Servicios/Diseño-y-desarrollo-web', WebDesign, name='web_design'),
    path('Servicios/Posicionamiento-web-organico', SEO, name='posicionamiento'),
    path('FAQ/', FAQ, name='faq'),
    path('Contacto/', Contacto, name='contacto'),
]
handler404 = error_404_view
