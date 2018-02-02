from django.db import models


class Webtoon(models.Model):
    webtoon_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

class Episode(models.Model):
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE)
    episode_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    created_date = models.CharField(max_length=200)
