import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    """
    Describes a question object for our poll
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """Return a string representation of a Question object"""
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        """Returns a bool indicating whether the question was published within the past day or not"""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Return a string representation of a Choice object"""
        return self.choice_text

