from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('choice', views.choice, name='choice'),
    path('create', views.create, name='sav_acc'),
    path('moneyOrder', views.moneyOrder, name='MO'),
    path('admin', views.admin, name='admin'),
    path('insurance', views.insurance, name='insurance'),
    path('letter',views.letter, name='letter'),
    path('e_bill',views.e_bill, name='e_bill'),
    path('addMoney',views.addMoney, name='addMoney'),
    path('withdraw',views.withdraw, name='withdraw'),
    path('status',views.status, name='status'),
]