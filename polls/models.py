import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    pollster = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    created_at = models.DateTimeField("created at", default=timezone.now())
    updated_at = models.DateTimeField("updated at", default=timezone.now())
    comment = models.CharField(max_length=200, blank=True)
    CATEGORY_CHOICES = [
        ("Categoria 1", "Pregunta directa"),
        ("Categoria 2", "Pregunta picante"),
        ("Categoria 3", "Pregunta incomoda"),
    ]
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="Categoria 1",
    )

    DAYS_PUBLISHED_RECENTLY = 1
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=self.DAYS_PUBLISHED_RECENTLY) <= self.pub_date <= now + datetime.timedelta(days=self.DAYS_PUBLISHED_RECENTLY)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField("created at", default=timezone.now())
    updated_at = models.DateTimeField("updated at", default=timezone.now())
    def __str__(self):
        return self.choice_text