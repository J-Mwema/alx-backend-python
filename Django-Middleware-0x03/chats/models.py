import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    """
    Custom User model using UUID instead of integer ID.
    Email must be unique.
    """
    # use a UUID primary key named `user_id` to match the spec
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)

    # compatibility: some code may expect `.id` attribute — provide a property alias
    @property
    def id(self):
        return self.user_id

    first_name = models.CharField(max_length=150, null=False, blank=False)
    last_name = models.CharField(max_length=150, null=False, blank=False)

    email = models.EmailField(unique=True, null=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    ROLE_CHOICES = [
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='guest')

    created_at = models.DateTimeField(default=timezone.now)

    # store password hash separately if desired by the spec (does not replace Django's password field)
    password_hash = models.CharField(max_length=128, null=False, blank=True)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.username} ({self.email})"


class Conversation(models.Model):
    """
    Chat conversation. Many users may participate.
    """
    # primary key named conversation_id to match the spec
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)

    @property
    def id(self):
        return self.conversation_id
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Conversation {self.id}"


class Message(models.Model):
    """
    Individual chat messages inside a conversation.
    """
    # primary key named message_id to match the spec
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)

    @property
    def id(self):
        return self.message_id
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages_sent")
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    message_body = models.TextField(null=False)
    sent_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.sender.username}: {self.message_body[:30]}"

