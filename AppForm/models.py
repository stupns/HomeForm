from django.db import models
from django.utils import timezone


class Message(models.Model):
    class Meta():
        db_table = 'HomeTable'

    author = models.ForeignKey('auth.User', on_delete=True)
    mes_title = models.CharField(max_length=128, blank=False)
    mes_text = models.TextField(max_length=342, blank=False)
    mes_created_date = models.DateTimeField(default=timezone.now)
    mes_public_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.mes_title