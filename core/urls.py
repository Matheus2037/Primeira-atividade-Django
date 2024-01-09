from django.urls import path

from .views import index, contato, produto


urlpatterns = [
    path('', index, name = 'index'),
    path('contato', contato, name= 'contato'),
    path('produtos/<int:pk>', produto, name='produto' ),
]