# backendApp/urls.py

from django.urls import path
from . import views
from .views import FavStockListCreateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update/<str:entryCompanyName>/', views.update, name='update'),
    path('delete_all/', views.delete_all, name='delete'),
    path('api/FavStocks/', FavStockListCreateView.as_view(), name='favstock-list-create'),
]
