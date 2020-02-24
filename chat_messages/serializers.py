from rest_framework import serializers
from .models import Message


class MessageDetailSerializer(serializers.ModelSerializer):
    message = serializers.RegexField(regex=r'^(.|\s)*\S(.|\s)*$', required=True, max_length=99)
    email = serializers.RegexField(regex=r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')

    class Meta:
        model = Message
        fields = 'id', 'email', 'message'
        read_only_fields = 'create_date', 'update_date'


class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = 'email', 'message'
        read_only_fields = 'create_date', 'update_date'
