from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
import cloudinary
import uuid
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

# Create your models here.
class posts_image(models.Model):
    title = models.CharField(null=True, blank=True)
    caption = models.TextField(null=True, blank=True)
    image = CloudinaryField('image')
    username = User.username
    datetime = models.DateTimeField(default=datetime.now())
    unique_id = models.UUIDField(primary_key = True, default= uuid.uuid4, editable = False)

    def __str__(self):
        return self.title

class posts_fb(models.Model):
    url = models.TextField(null=True, blank=True)
    username = User.username
    datetime = models.DateTimeField(default=datetime.now())
    unique_id = models.UUIDField(primary_key = True, default= uuid.uuid4, editable = False)

    def __str__(self):
        return self.url

class posts_text(models.Model):
    title = models.CharField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    username = User.username
    datetime = models.DateTimeField(default=datetime.now())
    unique_id = models.UUIDField(primary_key = True, default= uuid.uuid4, editable = False)

    def __str__(self):
        return self.title

class posts_order(models.Model):
    uid = models.UUIDField(null=True, blank=True)
