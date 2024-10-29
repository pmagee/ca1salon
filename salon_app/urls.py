from django.urls import path
from .views import ClientListView, ClientDetailView, ClientCreateView, HairdresserUpdateView, HairdresserDetailView,ChsListView
from . import views

urlpatterns = [
    path('', ClientListView.as_view(), name='c_list'),
    path('<int:pk>/', ClientDetailView.as_view(), name='c_detail'),
    path('new/', ClientCreateView.as_view(), name='c_new'),
    path('hd/<int:pk>/edit/', HairdresserUpdateView.as_view(), name='h_edit'),
    path('hd/<int:pk>/', HairdresserDetailView.as_view(), name='hd_detail'),
    path('chslist/', ChsListView.as_view(), name='chs_list'),
    path('query1/', views.query1, name='query1'),
    path('query2/', views.query2, name='query2'),

]