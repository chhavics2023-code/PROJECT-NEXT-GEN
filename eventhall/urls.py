from django .urls import path
from django.urls import  path, include
from django .http import HttpResponse
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('hall_details/', views.hall_details, name='hall_details'),

    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),

    path('halls/', views.halls, name='halls'),
    path('book/<int:id>/', views.book_hall, name='book_hall'),

    path('book/', views.book_hall, name='book_hall'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage-bookings/', views.manage_bookings, name='manage_bookings'),
    path('approve/<int:booking_id>/', views.approve_booking, name='approve_booking'),
    path('reject/<int:booking_id>/', views.reject_booking, name='reject_booking'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('halls/', views.halls, name='halls'),
]