from django.db import models

# Create your models here.
class Questions (models.Model):
    question_text = models.CharField(max_length=200)
    time_push = models.DateTimeField()

class Choices (models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    vote = models.IntegerField(default=0)