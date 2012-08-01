from django.db import models
from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile

class TodoProfile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True, verbose_name='user', related_name='mentoria_profile')
    favourite_snack = models.CharField('favourite snack', max_length=5)

class Task(models.Model):
    title = models.CharField(max_length=250)
    creation_date = models.DateTimeField(editable=False, auto_now=True)
    priority = models.IntegerField(default=0)
    user = models.ForeignKey(User, editable=False, blank=True, null=True)

    class Meta:        
        ordering = ('-priority', '-creation_date')
        verbose_name_plural = 'tasks'