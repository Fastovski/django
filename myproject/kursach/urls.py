#пути 
from django.urls import path
from . import views

urlpatterns=[
    path('register', views.register, name='register'),
    path ('login', views.login, name='login'),
    path ('', views.index, name='index'),
    path ('product', views.products, name='pr'),
    path ('ordername', views.ordername, name='ordername'),
    path ('ordercost', views.ordercost, name='ordercost'),
    path ('ordersupplier', views.ordersupplier, name='ordersupplier'),
    path ('infosupplier', views.infosupplier, name='infosupplier'),
    path ('expertmark', views.expertmark, name='expertmark'),
    path ('expertresult', views.expertresult, name='expertresult'),
    path ('logout', views.logout, name='logout'),
    path ('searchprod', views.searchprod, name='searchprod'),
    path ('search', views.search, name='search'),
    path ('logout', views.logout, name = 'logout'),
]