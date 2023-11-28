from django.urls import path
from . import views

urlpatterns = [
    path('',views.ussd_callback,name='ussd'),
    path('create/',views.create_student,name='create_student'),
]
