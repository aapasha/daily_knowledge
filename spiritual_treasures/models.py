from django.db import models
from django.db.models.functions import Length
from django.contrib.auth.models import User


class Excerpt(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    last_date_posted = models.DateTimeField(null=True)
    date_to_post = models.DateTimeField(null=True)
    content_length = models.functions.Length(content)
