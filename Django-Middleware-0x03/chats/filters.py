"""django-filters FilterSets for chats app.

Provides MessageFilter (filter by sender, conversation, start/end datetimes)
and ConversationFilter (filter by participant user id).
"""
try:
    import django_filters
    from django_filters import rest_framework as filters
except Exception:  # pragma: no cover - graceful fallback when package is missing
    django_filters = None
    filters = None

from .models import Message, Conversation


if django_filters and filters:
    class MessageFilter(filters.FilterSet):
        sender = filters.UUIDFilter(field_name='sender__id')
        conversation = filters.UUIDFilter(field_name='conversation__id')
        start = filters.DateTimeFilter(field_name='sent_at', lookup_expr='gte')
        end = filters.DateTimeFilter(field_name='sent_at', lookup_expr='lte')

        class Meta:
            model = Message
            fields = ['sender', 'conversation', 'start', 'end']


    class ConversationFilter(filters.FilterSet):
        participant = filters.UUIDFilter(field_name='participants__id')

        class Meta:
            model = Conversation
            fields = ['participant']
else:
    # Placeholders to avoid import-time failures; views will only use filters
    # if django-filters is installed.
    MessageFilter = None
    ConversationFilter = None
