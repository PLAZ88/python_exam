from __future__ import unicode_literals

from django.db import models
from ..log_reg.models import User

# Create your models here.

class WishManager(models.Manager):
    def process(self, id, name):

        user = User.objects.get(id=id)
        wish = self.create(item=name, creator=user)
        wish.users.add(user)

        return {'wish': wish}


class Wish(models.Model):
    item = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, related_name = "wishes", blank=True, null=True)
    users = models.ManyToManyField(User, related_name="user_wishes")
    objects = WishManager()
