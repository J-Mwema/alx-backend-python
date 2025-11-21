from rest_framework import permissions
from .models import Conversation, Message


class IsParticipantOfConversation(permissions.BasePermission):
	"""Allow access only to authenticated users who are participants of a conversation.

	- Requires authentication for all requests.
	- For object-level checks, ensures the user is part of the conversation (or the
	  conversation that a message belongs to).
	"""

	def has_permission(self, request, view):
		# Require authentication globally. View-level operations that need
		# additional checks are enforced in `has_object_permission` or by
		# filtering the queryset in the viewsets.
		return bool(request.user and request.user.is_authenticated)

	def has_object_permission(self, request, view, obj):
		# Conversation object: check participant membership
		if isinstance(obj, Conversation):
			return obj.participants.filter(pk=request.user.pk).exists()

		# Message object: check whether the user is participant of the message's conversation
		if isinstance(obj, Message):
			return obj.conversation.participants.filter(pk=request.user.pk).exists()

		# Fallback: deny
		return False
