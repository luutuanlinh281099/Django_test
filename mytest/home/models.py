from django.db import models

# Create your models here.
class Question (models.Model):
    question_id = models.IntegerField()
    question_text = models.CharField(max_length=200)
    time = models.DateTimeField

class Choice (models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    vote = models.IntegerField(default=0)