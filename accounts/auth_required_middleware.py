from django.contrib.auth.decorators import login_required
from django.conf import settings

public_paths = [
    '/',
    '/welcome/',
    '/accounts/login/',
    '/accounts/logout/',
    '/accounts/sign_up/',
]


class AuthRequiredMiddleware():

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path.startswith(settings.STATIC_URL) or request.path in \
                public_paths:
            return None
        else:
            return login_required(view_func)(request, *view_args,
                                             **view_kwargs)
