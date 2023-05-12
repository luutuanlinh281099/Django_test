from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    my_name = 'Linh ngoan hien'
    my_age = '24'
    my_asset = {'Thuy', 'Cua'}
    json = {'name' : my_name, 'age' : my_age, 'asset' : my_asset}
    return render(request, "home/home.html", json)