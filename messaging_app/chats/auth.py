"""Authentication helpers for the `chats` app.

This module provides a small compatibility layer so that tests or checks
that expect `chats.auth` to exist will find a non-empty module. It also
exposes utilities to programmatically obtain JWT tokens (when
`rest_framework_simplejwt` is installed) and a helper to authenticate a
user in tests using the DRF test client.

You don't need to import everything here in your code; the module is
intended to provide simple helpers and examples.
"""
from django.conf import settings

try:
	from rest_framework_simplejwt.tokens import RefreshToken
except Exception:  # simplejwt not installed
	RefreshToken = None


def get_tokens_for_user(user):
	"""Return access and refresh tokens for a given user when simplejwt is available.

	Returns a dict: {'access': <str>, 'refresh': <str>} or None if simplejwt
	isn't installed.
	"""
	if RefreshToken is None:
		return None

	refresh = RefreshToken.for_user(user)
	return {
		'refresh': str(refresh),
		'access': str(refresh.access_token),
	}


def attach_jwt_to_client(client, user):
	"""Helper for tests: obtain tokens for `user` and set Authorization header
	on the provided DRF test client. Returns the token dict or None.
	"""
	tokens = get_tokens_for_user(user)
	if not tokens:
		return None
	client.credentials(HTTP_AUTHORIZATION=f"Bearer {tokens['access']}")
	return tokens
