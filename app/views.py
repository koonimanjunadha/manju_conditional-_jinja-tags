from django.shortcuts import render

# Create your views here.
def condition(request):
    d={
        'a':30,'b':25,'c':12,
    }
    return render(request,'condition.html',d)