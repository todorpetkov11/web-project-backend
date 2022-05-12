from django.urls import path
from users.views import UsersView, RetrieveUser

urlpatterns = [
    path('', UsersView.as_view()),
    path('<str:username>', RetrieveUser.as_view()),
]