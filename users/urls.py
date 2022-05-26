from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import UsersView, RetrieveUpdateDestroyUserView, MyObtainTokenPairView, RegisterView

urlpatterns = [
    path('', UsersView.as_view()),
    path('<int:pk>', RetrieveUpdateDestroyUserView.as_view()),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='user_register')
]
