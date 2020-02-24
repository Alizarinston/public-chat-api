from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .serializers import MessageDetailSerializer, MessageListSerializer
from .models import Message


class SmallPagesPagination(PageNumberPagination):
    page_size = 10


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageDetailSerializer


class MessageListView(generics.ListAPIView):
    serializer_class = MessageListSerializer
    queryset = Message.objects.all()
    pagination_class = SmallPagesPagination


class MessageDetailView(generics.RetrieveAPIView):
    serializer_class = MessageDetailSerializer
    queryset = Message.objects.all()
