from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('eventlist', views.eventlist, name='eventlist'),
    path('eventcreate', views.eventcreate, name='eventcreate'),
    path('dashindex', views.dashindex, name='dashindex'),
    path('editevent', views.editevent, name='editevent'),
    path('eventlistAdmin', views.eventlistAdmin, name='eventlistAdmin'),
    path('Bookindex', views.Bookindex, name='Bookindex'),
    path('eventdelete', views.eventdelete, name='eventdelete'),
    path('faqindex', views.faqindex, name='faqindex'),
    path('feedback', views.feedback, name='feedback'),
    path('QR1index', views.QR1index, name='QR1index'),
    path('QR2index', views.QR2index, name='QR2index'),
    path('QR3index', views.QR3index, name='QR3index'),
    

]
