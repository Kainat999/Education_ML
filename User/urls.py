from django.urls import path
from . import views

urlpatterns = [
    # API views
    path('api-register/', views.user_registration, name='api-user-registration'),
    path('api-login/', views.user_login, name='api-user-login'),
    path('api-logout/', views.user_logout, name='api-user-logout'),
    path('api-profile/', views.user_profile, name='api-user-profile'),

    # Template views
    path('register/', views.register_view, name='register-view'),
    path('login/', views.login_view, name='login-view'),
    path('profile/', views.profile_view, name='profile-view'),
    path('',views.home, name='home')
]
