from django.conf.urls import url
from . import views
from general.views import contactFormView

urlpatterns = [
    # general/
    url(r'^$', views.index, name='index'),
    url(r'^service/$', views.service, name='service'),
    url(r'about/$', views.about, name='about'),
    url(r'training/$', views.training, name='training'),
    url(r'gallery/$', views.gallery, name='gallery'),
    url(r'contact/', contactFormView.as_view(), name='contactform'),
    #url(r'contact/thanks/', views.thanks, name='thanks'),
]
