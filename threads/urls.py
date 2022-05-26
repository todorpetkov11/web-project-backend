from django.urls import path

from threads.views import AllThreads, RetrieveThreadUpdateDelete, ThreadsByUser

urlpatterns = [
    path('', AllThreads.as_view()),
    path('<int:pk>/', RetrieveThreadUpdateDelete.as_view()),
    path('user/<str:username>/', ThreadsByUser.as_view()),
]
