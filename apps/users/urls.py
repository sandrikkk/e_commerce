from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from apps.users.views import LoginUser, RegistrationUserApiView

urlpatterns = [
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginUser.as_view(), name='login'),
    path('registration/', RegistrationUserApiView.as_view(), name='registration')
]
