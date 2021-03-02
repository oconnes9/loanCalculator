from django.shortcuts import render
from .forms import CalcForm
def homepage(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        form = CalcForm()
        formDict = {
            'form':form
        }
    return render(request,'index.html',context=formDict)

