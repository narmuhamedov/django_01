from django.urls import path
from  . import views

urlpatterns = [
    path('shows/', views.shows_all, name='shows_all'),
    path('shows/<int:id>/', views.shows_detail, name='shows_detail'),
    path('shows/<int:id>/update/', views.show_update, name='update-show'),
    path('add-shows/', views.add_show, name='add-show'),


]