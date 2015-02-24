# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.core.urlresolvers import reverse

from ...models import Key


class Command(BaseCommand):
    help = "Generate login keys for users"

    def add_arguments(self, parser):
        parser.add_argument('user', help='Generate key for this user.')

    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.get(username=options['user'])
        key = Key.objects.create(user=user)
        url = reverse('sshlogin', args=[key.key])
        self.stdout.write('Login at\n\n\thttp://localhost:8000{}\n\n'.format(url))
