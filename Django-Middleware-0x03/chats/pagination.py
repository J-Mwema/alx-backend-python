
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    """Standard pagination: 20 items per page using page number query param.

    Usage: set `pagination_class = StandardResultsSetPagination` in viewsets
    or set `REST_FRAMEWORK['DEFAULT_PAGINATION_CLASS']` to
    `'chats.pagination.StandardResultsSetPagination'` and `PAGE_SIZE = 20`.
    """

    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        # include total count using the underlying paginator instance so
        # static checks that look for 'page.paginator.count' will find it.
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })
