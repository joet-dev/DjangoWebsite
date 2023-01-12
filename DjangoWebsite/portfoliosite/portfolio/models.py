import datetime

from django.db import models
from django.utils import timezone


class PortfolioItem(models.Model):
    item_title = models.CharField(max_length=200)
    item_date = models.DateTimeField('date published')
    item_hits = models.IntegerField(default=0)
    item_img_id = models.CharField(max_length=150)
    item_details = models.TextField('details', default="There are no details currently. Sorry!")

    def __str__(self):
        return self.item_title
