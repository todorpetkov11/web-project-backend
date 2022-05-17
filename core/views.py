from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from core.models import CommentsModel, LikesModel
from core.serializers import CommentsSerializer, LikesSerializer


class CommentsByThread(ListCreateAPIView):
    serializer_class = CommentsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, thread=self.request.threadId)

    def get_queryset(self):
        thread_id = self.kwargs['thread_id']
        return CommentsModel.objects.filter(thread=thread_id)


class CommentView(RetrieveUpdateDestroyAPIView):
    queryset = CommentsModel.objects.all()
    serializer_class = CommentsSerializer


class CommentsByUser(ListAPIView):
    serializer_class = CommentsSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return CommentsModel.objects.filter(id=user_id)


class LikesByThread(ListCreateAPIView):
    serializer_class = LikesSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, thread=self.request.threadId)

    def get_queryset(self):
        thread_id = self.kwargs['thread_id']
        return LikesModel.objects.filter(thread=thread_id)


class LikeView(RetrieveUpdateDestroyAPIView):
    queryset = LikesModel.objects.all()
    serializer_class = LikesSerializer


class LikesByUser(ListAPIView):
    serializer_class = LikesSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return LikesModel.objects.filter(id=user_id)


