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
    # writable/validated field for message body
    message_body = serializers.CharField(max_length=5000)
    class Meta:
        model = Message
        fields = ['message_id', 'id', 'sender', 'message_body', 'sent_at', 'conversation']
        read_only_fields = ['id', 'sent_at', 'sender']

    def validate_message_body(self, value):
        """Ensure message body is not empty and not just whitespace."""
        if not value or not value.strip():
            raise serializers.ValidationError("message_body cannot be empty")
        return value


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)  # nested messages
    conversation_id = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    # include a computed field with the last message in the conversation
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'id', 'participants', 'messages', 'created_at']
        read_only_fields = ['conversation_id', 'id', 'created_at', 'messages']

    def get_last_message(self, obj):
        last = obj.messages.order_by('-sent_at').first()
        if not last:
            return None
        # reuse MessageSerializer for consistent output
        return MessageSerializer(last, context=self.context).data

