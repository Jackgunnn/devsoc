from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer


def home(request):
    questions = Question.objects.all()
    return render(request, 'home.html', {'questions':questions})


def view_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'viewanswer.html', {'question': question, 'answers': answers})


def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')  # Redirect to wherever you want
    else:
        form = QuestionForm()
    return render(request, 'question.html', {'form': form})


def add_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return render(request, 'anssuccess.html')  # Redirect to question detail page
    else:
        form = AnswerForm()
    return render(request, 'addanswer.html', {'form': form})

