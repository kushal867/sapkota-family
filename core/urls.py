from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # Invitation URLs
    path('invitations/', views.invitation_list, name='invitation_list'),
    path('invitations/<int:pk>/', views.invitation_detail, name='invitation_detail'),
    path('invitations/create/', views.invitation_create, name='invitation_create'),
    path('invitations/<int:pk>/update/', views.invitation_update, name='invitation_update'),
    path('invitations/<int:pk>/delete/', views.invitation_delete, name='invitation_delete'),
    
    # Birthday URLs
    path('birthdays/', views.birthday_list, name='birthday_list'),
    path('birthdays/<int:pk>/', views.birthday_detail, name='birthday_detail'),
    path('birthdays/create/', views.birthday_create, name='birthday_create'),
    path('birthdays/<int:pk>/update/', views.birthday_update, name='birthday_update'),
    path('birthdays/<int:pk>/delete/', views.birthday_delete, name='birthday_delete'),
    
    # Gallery URLs
    path('gallery/', views.gallery_list, name='gallery_list'),
    path('gallery/<int:pk>/', views.gallery_detail, name='gallery_detail'),
    path('gallery/create/', views.gallery_create, name='gallery_create'),
    path('gallery/<int:pk>/update/', views.gallery_update, name='gallery_update'),
    path('gallery/<int:pk>/delete/', views.gallery_delete, name='gallery_delete'),
]