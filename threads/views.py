from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from threads.models import ThreadModel
from threads.serializers import ThreadSerializer


class AllThreads(ListCreateAPIView):
    queryset = ThreadModel.objects.all()
    serializer_class = ThreadSerializer


class RetrieveThreadUpdateDelete(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ThreadModel.objects.all()
    serializer_class = ThreadSerializer
