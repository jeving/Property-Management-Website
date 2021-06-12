from django.urls import path

from . import views 


urlpatterns = [
    path('', views.index, name='addpropertys'),
    path('<int:addproperty1_id>', views.addproperty1, name='addproperty1'),
    path('addproperty', views.addproperty, name='addproperty'),
    path('properties1', views.properties1, name='properties1'),
]