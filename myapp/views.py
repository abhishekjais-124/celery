from django.shortcuts import render
from myapp.tasks import add

def index(request):
    v = add.delay(10, 20)
    print("Results: ", v)
    return render(request, "myapp/home.html")