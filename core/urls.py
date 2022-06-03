from django.urls import path

from core.views import CommentsByThread, CommentsByUser, CommentView, LikeView, LikesByThread, LikesByUser, \
    AsideListView, AsideDestroy

urlpatterns = [
    path('comments/<int:pk>/', CommentView.as_view()),
    path('comments/thread/<int:thread_id>/', CommentsByThread.as_view()),
    path('comments/user/<int:user_id>/', CommentsByUser.as_view()),
    path('likes/<int:pk>/', LikeView.as_view()),
    path('likes/thread/<int:thread_id>/', LikesByThread.as_view()),
    path('likes/user/<int:user_id>/', LikesByUser.as_view()),
    path('aside/', AsideListView.as_view()),
    path('aside/<int:pk>/', AsideDestroy.as_view())
]
