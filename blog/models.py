from django.db import models
from django.utils import timezone
from django.db.models.functions import Length


class Post(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # date_to_post = models.DateTimeField(blank=True)
    content_length = models.functions.Length(content)
    SPIRITUAL_TREASURES = 'ST'
    DAILY_HADITH = 'DH'
    CATEGORY_CHOICES = [
        (SPIRITUAL_TREASURES, 'Spiritual Treasures'),
        (DAILY_HADITH, 'Daily Hadith')]
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES)

    def is_daily_hadith(self):
        return self.category == self.DAILY_HADITH
