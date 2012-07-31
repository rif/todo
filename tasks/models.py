from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    title = models.CharField(max_length=250)
    creation_date = models.DateTimeField(editable=False, auto_now=True)
    priority = models.IntegerField(default=0)
    user = models.ForeignKey(User, editable=False, blank=True, null=True)

    class Meta:        
        ordering = ('-priority', '-creation_date')
        verbose_name_plural = 'tasks'