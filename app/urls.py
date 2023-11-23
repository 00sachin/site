from.import views
from django.urls import path ,include


urlpatterns = [
    
    path('', views.index,name='index'),
    path('resume', views.resume,name='resume'),
    path('portfolio', views.portfolio,name='portfolio'),
    path('contacts', views.contacts,name='contacts'),
    path('form', views.my_form, name='form'),



]
