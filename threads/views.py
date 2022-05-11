from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView

from threads.models import ThreadModel
from threads.serializers import ThreadSerializer


class AllThreads(ListCreateAPIView):
    queryset = ThreadModel.objects.all()
    serializer_class = ThreadSerializer


class RetrieveThreadUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = ThreadModel.objects.all()
    serializer_class = ThreadSerializer