from django.db import models
from django.utils.timezone import now


class BaseTimeModel(models.Model):
    tick = models.IntegerField(default=0)
    tick_in_seconds = models.IntegerField(default=1)
    last_update = models.DateTimeField(default=now)
    start_date = models.DateTimeField(default=now)

    class Meta:
        abstract = True
