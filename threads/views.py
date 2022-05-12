from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from threads.models import ThreadModel
from threads.permissions import IsOwnerOrReadOnly
from threads.serializers import ThreadSerializer


class AllThreads(ListCreateAPIView):
    queryset = ThreadModel.objects.all()
    serializer_class = ThreadSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RetrieveThreadUpdateDelete(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = ThreadModel.objects.all()
    serializer_class = ThreadSerializer
