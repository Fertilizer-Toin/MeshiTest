from django.urls import path
from . import views
app_name = 'ans'
urlpatterns = [
    path('templates/', views.index_template, name='index_template'),
    path('question/',views.Questions,name ='Questions'),
    path('question/',views.answer1,name ='answer1'),
    ]
