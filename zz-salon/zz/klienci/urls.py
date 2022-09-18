from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('klienci/', views.pets, name='pets'),
    path('klienci/<int:zwierze_id>/', views.detail, name='detail'),
    path('kalendarz/', views.calendar, name='calendar'),
    path('search/', views.search, name='search'),
    path('klienci/edit/<int:zwierze_id>/', views.edit_pet, name='edit_pet'),
    path('add_visit/', views.add_visit, name='add_visit'),
    path('visit/<int:visit_id>/', views.edit_visit, name='edit_visit'),
]