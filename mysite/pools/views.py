from django.shortcuts import render
from .models import Question


def view_index(request):
    questions = Question.objects.all()

    return render(request, 'index.html', {'questions' : questions})


def view_questions(request, id):
    question = Question.objects.get(id)

    return render(request, 'question.html', {'question' : question})