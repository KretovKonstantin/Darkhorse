from django.urls import path, include
from users import views


app_name = 'users'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('accounts/', include('allauth.urls')),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('users-cart/', views.UserCartView.as_view(), name='users_cart'),
    path('logout/', views.logout, name='logout'),
    path('restore/', views.PasswordRestoreView.as_view(), name='restore_password'),
]