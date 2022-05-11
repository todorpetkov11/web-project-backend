from django.urls import path

from threads.views import AllThreads, RetrieveThreadUpdateDelete

urlpatterns = [
    path('', AllThreads.as_view()),
    path('<int:pk>/', RetrieveThreadUpdateDelete.as_view())
]
