from django.urls import path
from .views import RegisterUserView, UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)

urlpatterns = [
    path('user', UserView.as_view()),
    path('register', RegisterUserView.as_view()),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', TokenBlacklistView.as_view(), name='token_blacklist'),
]