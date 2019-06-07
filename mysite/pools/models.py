from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    closed = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'

    def salvar(self):
        self.save()

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ManyToManyField('Question', related_name='choices_question')
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Escolha'
        verbose_name_plural = 'Escolhas'

    def __str__(self):
        return self.choice_text