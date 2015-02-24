import datetime

from django.contrib.auth.backends import ModelBackend
from django.shortcuts import get_object_or_404
from django.utils.timezone import now

from .models import Key


class SSHLoginBackend(ModelBackend):
    def authenticate(self, key_string=None, **kwargs):
        if key_string is None:
            return

        qs = Key.objects.select_related('user')
        valid_until = now() - datetime.timedelta(seconds=10)
        key = get_object_or_404(qs, key=key_string, created__gte=valid_until)
        return key.user
