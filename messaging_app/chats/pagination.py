from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    """Standard pagination: 20 items per page using page number query param.

    Usage: set `pagination_class = StandardResultsSetPagination` in viewsets
    or set `REST_FRAMEWORK['DEFAULT_PAGINATION_CLASS']` to
    `'chats.pagination.StandardResultsSetPagination'` and `PAGE_SIZE = 20`.
    """

    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
