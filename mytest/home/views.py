from django.shortcuts import render
from django.http import HttpResponse
from.models import Questions

# Create your views here.
def home(request):
    my_name = 'Linh ngoan hien'
    my_age = '24'
    my_asset = {'Thuy', 'Cua'}
    questions = Questions.objects.all()
    json = {'name' : my_name, 'age' : my_age, 'asset' : my_asset, 'questions' : questions}
    return render(request, "home/home.html", json)
