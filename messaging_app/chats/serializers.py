from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'created_at']


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)  # include sender details in response

    class Meta:
        model = Message
        fields = ['id', 'sender', 'message_body', 'sent_at', 'conversation']
        read_only_fields = ['id', 'sent_at', 'sender']


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)  # nested messages

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'messages', 'created_at']
        read_only_fields = ['id', 'created_at', 'messages']

