from django.urls import path
from . import views

app_name = 'banco'
urlpatterns =[
    path('getBanco', views.bancoList, name='listagem'),
    path('postBanco', views.bancoPost, name='envio'),
    path('putBanco/<str:pk>', views.bancoPut, name='atualizar'),
    path('deleteBanco/<str:pk>', views.bancoDelete, name='deletar'),

]
