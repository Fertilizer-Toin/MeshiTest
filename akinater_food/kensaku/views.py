from django.shortcuts import render
from .models import choices
# Create your views here.
def index_template(request):
    data = choices.objects.all(),
    params = {'message':'データ一覧','data':data}
    return render(request,'index.html',params)
