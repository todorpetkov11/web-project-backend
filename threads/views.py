from django.db.models import Q
from rest_framework import filters
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from threads.models import ThreadModel
from threads.serializers import ThreadSerializer


class AllThreads(ListCreateAPIView):
    serializer_class = ThreadSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['game', 'genre']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = ThreadModel.objects.all()
        genre = self.request.query_params.get('genre')
        game = self.request.query_params.get('game')
        search = self.request.query_params.get('search')
        if genre is not None:
            queryset = queryset.filter(genre=genre)

        if game is not None:
            queryset = queryset.filter(game=game)

        if search is not None:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(body__icontains=search) | Q(game__icontains=search) |
                Q(description__icontains=search) | Q(genre__icontains=search))
        return queryset


class RetrieveThreadUpdateDelete(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ThreadModel.objects.all()
    serializer_class = ThreadSerializer


class ThreadsByUser(ListAPIView):
    serializer_class = ThreadSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return ThreadModel.objects.filter(author=username)
