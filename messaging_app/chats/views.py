from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, Conversation, Message
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing and creating conversations.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    # enable simple filtering/searching on conversations
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['participants__username']
    ordering_fields = ['created_at']

    @action(detail=True, methods=['post'])
    def add_participants(self, request, pk=None):
        """
        Custom action to add participants to a conversation.
        """
        conversation = self.get_object()
        user_ids = request.data.get('user_ids', [])

        if not user_ids:
            return Response({"detail": "No user_ids provided"}, status=status.HTTP_400_BAD_REQUEST)

        users = User.objects.filter(id__in=user_ids)
        conversation.participants.add(*users)
        conversation.save()

        serializer = self.get_serializer(conversation)
        return Response(serializer.data)


class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing messages and sending new messages.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['message_body', 'sender__username']
    ordering_fields = ['sent_at']

    def create(self, request, *args, **kwargs):
        """
        Override create to automatically set sender.
        Expecting 'conversation' and 'message_body' in request data.
        """
        sender = request.user  # assumes authenticated user
        conversation_id = request.data.get('conversation')
        message_body = request.data.get('message_body')

        if not conversation_id or not message_body:
            return Response({"detail": "conversation and message_body are required"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            conversation = Conversation.objects.get(id=conversation_id)
        except Conversation.DoesNotExist:
            return Response({"detail": "Conversation not found"}, status=status.HTTP_404_NOT_FOUND)

        message = Message.objects.create(
            sender=sender,
            conversation=conversation,
            message_body=message_body
        )

        serializer = self.get_serializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

