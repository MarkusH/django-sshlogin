from django.conf import settings
from django.db import models, transaction
from django.utils.crypto import get_random_string
from django.utils.timezone import now


class Key(models.Model):
    key = models.CharField(max_length=254, unique=True, db_index=True)
    created = models.DateTimeField(default=now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def save(self, *args, **kwargs):
        if self.pk:
            return
        with transaction.atomic():
            self.key = get_random_string(254)
            while Key.objects.filter(key=self.key).exists():
                self.key = get_random_string(254)
            super(Key, self).save(*args, **kwargs)

