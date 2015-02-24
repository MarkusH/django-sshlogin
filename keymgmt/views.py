from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, get_object_or_404

from .models import Key


def sshlogin(request, key_string):
    user = authenticate(key_string=key_string)
    login(request, user)
    return redirect('admin:index')
