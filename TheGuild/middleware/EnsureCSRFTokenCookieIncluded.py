from django.utils.deprecation import MiddlewareMixin
from django.middleware.csrf import get_token

class EnsureCsrfCookieMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == 'GET':
            get_token(request)
        return None