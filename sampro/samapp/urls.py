from .views import *
from rest_framework import routers
from django.urls import path, include
from django.contrib.auth import views as auth
from rest_framework.authtoken import views
router = routers.DefaultRouter()

urlpatterns = [
    path('RegisterView/', RegisterView.as_view(), name='RegisterView'),
    path('loginAPIView/', loginAPIView.as_view(), name='loginAPIView'),
    path('VerifyEmail/', VerifyEmail.as_view(), name='email-verify'),
	path('api/',include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token,name='api-token-auth'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),

]
