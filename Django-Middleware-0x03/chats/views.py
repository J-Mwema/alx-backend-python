from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, Conversation, Message
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOfConversation
from rest_framework.permissions import IsAuthenticated
from .pagination import StandardResultsSetPagination
from . import filters as chat_filters


class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing and creating conversations.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
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

    def get_queryset(self):
        # Limit conversations to those the requesting user participates in
        user = getattr(self.request, 'user', None)
        if not user or not user.is_authenticated:
            return Conversation.objects.none()
        return Conversation.objects.filter(participants=user).distinct()

    # Attach a filterset when django-filters is available
    if getattr(chat_filters, 'ConversationFilter', None):
        filterset_class = chat_filters.ConversationFilter
    pagination_class = StandardResultsSetPagination


class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing messages and sending new messages.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = StandardResultsSetPagination
    # attach filterset_class only when available
    if getattr(chat_filters, 'MessageFilter', None):
        filterset_class = chat_filters.MessageFilter
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
        # Ensure sender is a participant of the conversation
        if not conversation.participants.filter(pk=sender.pk).exists():
            return Response({"detail": "You are not a participant of this conversation"}, status=status.HTTP_403_FORBIDDEN)
        message = Message.objects.create(
            sender=sender,
            conversation=conversation,
            message_body=message_body
        )

        serializer = self.get_serializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        # Limit messages to those in conversations the requesting user participates in
        user = getattr(self.request, 'user', None)
        if not user or not user.is_authenticated:
            return Message.objects.none()
        return Message.objects.filter(conversation__participants=user).distinct()

