from django.shortcuts import render
from .models import Quiz
# Create your views here.

def quiz_list_view(request):
    quizzes = Quiz.objects.all()
    return render(request, 'assessments/quiz_list.html', {'quizzes': quizzes})

def quiz_detail_view(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    return render(request, 'assessments/quiz_detail.html', {'quiz': quiz})