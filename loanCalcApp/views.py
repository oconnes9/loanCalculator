from django.shortcuts import render
from .forms import CalcForm
from . import utils

def homepage(request):
    if request.method == "POST":
        form = CalcForm(request.POST)
        if form.is_valid():
            loanAmount = form.cleaned_data.get("loanAmount")
            numPayments = form.cleaned_data.get("numPayments") or None
            monthlyRepayment = form.cleaned_data.get("monthlyRepayment") or None

            results = utils.handleForm(loanAmount, numPayments, monthlyRepayment)
            formDict = {
                "form": form,
                "loanAmount": form.cleaned_data.get("loanAmount")
            }

            formDict.update(results)
        else:
            formDict = {
                'form': form
            }
        return render(request, 'index.html', context=formDict)


    elif request.method == "GET":
        form = CalcForm()
        formDict = {
            'form': form
        }
    return render(request,'index.html',context=formDict)

