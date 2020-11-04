from django.conf.urls import url
from CitasMedicas import views

urlpatterns=[
    url(r'^persona/$',views.personaApi),
    url(r'^persona/([0-9]+)$',views.personaApi),

    url(r'^consultorio/$',views.consultorioApi),
    url(r'^consultorio/([0-9]+)$',views.consultorioApi)
]