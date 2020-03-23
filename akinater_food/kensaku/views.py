from django.shortcuts import render
from .models import choices
# Create your views here.
def index_template(request):
    myapp_data = {
      'app': 'Django',
      }
    return render(request,'index.html',myapp_data)
def questions(request):
    questions_data = {'questions':[],}
    return render(request,'question.html',questions_data)
def answer(request):
    if request.method == 'PODT':
        
    
