from django.db import models

# Create your models here.

class AnimeKnowledgeUnit(models.Model):
    path = models.FileField("Anime knowledge unit", upload_to="")
