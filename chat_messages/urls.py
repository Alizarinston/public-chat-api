from django.urls import path
from .views import MessageCreateView, MessageListView, MessageDetailView


app_name = 'chat_messages'
urlpatterns = [
    path('', MessageCreateView.as_view(), name='message_create_url'),
    path('list/', MessageListView.as_view()),
    path('single/<int:pk>/', MessageDetailView.as_view()),
]
