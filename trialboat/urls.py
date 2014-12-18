from django.conf.urls import patterns, include, url
from django.contrib import admin

from mainapp import views


urlpatterns = patterns('',
                       url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.home, name='home'),
    url(r'^payment/', views.payment, name='payment'),
    url(r'^register/', views.register, name='register')
    )