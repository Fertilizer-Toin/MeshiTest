from django.shortcuts import render
from django.db import connection
from .models import choices,questions
import random
# Create your views here.
kuji = random.randint(1,1)
question = questions.objects.get(pk=kuji)
def index_template(request):
    myapp_data = {
        'app':'Django'
    }
    return render(request,'index.html',myapp_data)
def Questions(request):
    q ={
        'question':question.question_text,
        'choice_1':question.answer1_text,
        'answer1_column ':question.answer1_column,
        'answer1_get_ans':question.answer1_get_ans,
        'choice_2':question.answer2_text,
        'answer2_column ':question.answer2_column,
        'answer2_get_ans':question.answer2_get_ans,
        'choice_3':question.answer3_text,
        'answer3_column ':question.answer3_column,
        'answer3_get_ans':question.answer3_get_ans,
        'choice_4':question.answer4_text,
        'answer4_column ':question.answer4_column,
        'answer4_get_ans':question.answer4_get_ans,

    }
    return render(request,'question.html',q)
def answer1(request):
    answer = []
    if request.method == 'POST':
        if 'one' in request.POST:
            answer[2]+=question[kuji][3]
        elif 'two' in request.POST:
            answer[5]+=question[kuji][3]
        elif  'three' in request.POST:
            answer[8]+=question[kuji][3]
        elif 'four' in request.POST:
            answer[9]+=question[kuji][3]
