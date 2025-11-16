from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    # expose both `user_id` and a compat `id` (property) which returns the same value
    user_id = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ['user_id', 'id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'created_at']


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)  # include sender details in response
    # expose message_id for clarity
    message_id = serializers.ReadOnlyField()
    class Meta:
        model = Message
        fields = ['message_id', 'id', 'sender', 'message_body', 'sent_at', 'conversation']
        read_only_fields = ['id', 'sent_at', 'sender']


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)  # nested messages
    conversation_id = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'id', 'participants', 'messages', 'created_at']
        read_only_fields = ['conversation_id', 'id', 'created_at', 'messages']

