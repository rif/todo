from django.db import models
from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile

class TodoProfile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True, verbose_name=_('user'), related_name='mentoria_profile')
    favourite_snack = models.CharField(_('favourite snack'), max_length=5)
