from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    closed = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Escolha'
        verbose_name_plural = 'Escolhas'

    def __str__(self):
        return self.choice_text