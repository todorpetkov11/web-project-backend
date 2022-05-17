from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from threads.models import ThreadModel
from threads.permissions import IsOwnerOrReadOnly
from threads.serializers import ThreadSerializer


class AllThreads(ListCreateAPIView):
    serializer_class = ThreadSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = ThreadModel.objects.all()
        genre = self.request.query_params.get('genre')
        game = self.request.query_params.get('game')
        if genre is not None:
            queryset = queryset.filter(genre=genre)

        if game is not None:
            queryset = queryset.filter(game=game)
        return queryset



class RetrieveThreadUpdateDelete(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = ThreadModel.objects.all()
    serializer_class = ThreadSerializer
