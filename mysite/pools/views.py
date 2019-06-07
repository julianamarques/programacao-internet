from django.shortcuts import render
from .models import Question, Choice


def view_index(request):
    questions = Question.objects.order_by('-pub_date')

    return render(request, 'index.html', {'questions' : questions})


def view_question(request, id):
    question = Question.objects.get(id=id)
    choices = Choice.objects.filter(question__id=id)

    return render(request, 'question.html', 
    {
        'question' : question, 
        'choices' : choices
    })

def view_result(request, id):
    question = Question.objects.get(id=id)
    choices = Choice.objects.filter(question__id=id)

    return render(request, 'result.html', 
    {
        'question' : question,
        'choices' : choices
    })