from django.urls import path
from .views import IndexView, AboutView, ContactView
# from django.views.decorators.cache import cache_page
from .views import DeliveryView
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('delivery/', DeliveryView.as_view(), name='delivery'),
]

