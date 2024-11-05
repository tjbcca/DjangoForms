from django.shortcuts import render
from app.forms import *

def how_old(request):
    form = HowOld(request.GET)
    if form.is_valid():
        age_in = int(form.cleaned_data['year'])
        birth = int(form.cleaned_data['birth'])
        #How Old
        if age_in !="" and birth !="":
            old = (int(age_in) - int(birth))
        else:
            old = None
        return render(request, 'howOld.html', {'form':form, 'old':old})
    else:
        return render(request, 'howOld.html', {'form':form})
def order(request):
    form = CANITAKEYOURORDER(request.GET)
    if form.is_valid():
        burgers = int(form.cleaned_data['burgers'])
        drinks = int(form.cleaned_data['drinks'])
        fries = int(form.cleaned_data['fries'])
        #Can I Take Your Order
        if burgers !="" and fries !="" and drinks !="":
            order_total = str("${:.2f}".format((float(burgers) * 4.5) + (float(fries) * 1.5) + (float(drinks) * 1)))
        else:
            order_total = None
        return render(request, 'order.html', {'form':form, 'order_total':order_total})
    else:
        return render(request, 'order.html', {'form':form})
def root(request):
    form = HeyYou(request.GET)
    if form.is_valid():
        xname = form.cleaned_data['name']
        #Hey You
        if xname !="":
            name = xname
        else:
            name = None
        return render(request, 'root.html', {'name':name, 'form':form})
    else:
        return render(request, 'root.html', {'form':form})
def front_times(request):
    form = FontTimes(request.GET)
    if form.is_valid():
        word = str(form.cleaned_data['word'])
        n = int(form.cleaned_data['n'])
        if word !="" and n !="":
            front_len = 3
            if front_len > len(word):
                front_len = len(word)
            front = word[:front_len]
            result = ""
            for i in range(n):
                result += front
        else:
            result = None
        return render(request, 'frontTimes.html', {'form':form, 'result':result})
    else:
        return render(request, 'frontTimes.html', {'form':form})
def teen_sum(request):
    form = TeenSum(request.GET)
    if form.is_valid():
        a = form.cleaned_data['a']
        b = form.cleaned_data['b']
        c = form.cleaned_data['c']
        if a !="" and b !="" and c !="":
            numbers = [int(a), int(b), int(c)]
            total = 0
            for number in numbers:
                if number <= 12:
                    total += number
        else:
            total = None
        return render(request, 'teenSum.html', {'total':total, 'form':form})
    else:
        return render(request, 'teenSum.html', {'form':form})
def xyz_there(request):
    form = XYZthere(request.GET)
    if form.is_valid():
        if request.GET['string'] !="":
            s = form.cleaned_data['string']
            result = False
            if s[:3] == "xyz":
                result = True
            for i in range(1, len(s) - 2):
                if s[i-1] != '.' and s[i:i+3] == "xyz":
                    result = True
        else:
            result = None
        return render(request, 'xyzThere.html', {'result':result, 'form':form})
    else:
        return render(request, 'xyzThere.html', {'form':form})
def centered_average(request):
    form = Median(request.GET)
    if form.is_valid():
        if request.GET['array'] !="":
            array = form.cleaned_data['array'].split()
            n = len(array)
            if n % 2 == 1:
                result = array[n // 2]
            else:
                mid1 = int(array[n // 2 - 1])
                mid2 = int(array[n // 2])
                result = ((mid1 + mid2) / 2)
        else:
            result = None
        return render(request, 'centeredAverage.html', {'result':result, 'form':form})
    else:
        return render(request, 'centeredAverage.html', {'form':form})