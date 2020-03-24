from django.shortcuts import render
from .models import choices
import random
# Create your views here.
#このリストややこしいな。二次元配列です。[問題,ボタン１の解答,聞いた答えのカラムの番号。例）味=16,解答　甘み =1,ボタン２の解答,カラム,解答,ボタン３の解答,カラム,解答,ボタンの解答４カラム,解答,]
question_data =[["果物カゴがあります。あなたはどれを選ぶ？","みかん",16,"12","カカオ",16,"3","なぜか混じってた唐辛子",16,"6","全部!",16,"5"]]
kuji = random.randint(0,0)
question = question_data[kuji]
def index_template(request):
    myapp_data = {
        'app':'Django'
    }
    return render(request,'index.html',myapp_data)
def questions(request):
    q ={'question':question}
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
