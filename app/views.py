from django.shortcuts import render

def root(request):
    if request.GET:
        #Hey You
        if request.GET['name'] !="":
            name = request.GET['name']
        else:
            name = None
        #How Old 
        if request.GET['age-in'] !="" and request.GET['birth'] !="":
            old = (int(request.GET['age-in']) - int(request.GET['birth']))
        else:
            old = None
        #Can I Take Your Order
        if request.GET['burgers'] !="" and request.GET['fries'] !="" and request.GET['drinks'] !="":
            order_total = str("${:.2f}".format((float(request.GET['burgers']) * 4.5) + (float(request.GET['fries']) * 1.5) + (float(request.GET['drinks']) * 1)))
        else:
            order_total = None
        return render(request, 'root.html', {'name':name, 'old':old, 'order_total':order_total})
    else:
        return render(request, 'root.html')
def front_times(request):
    if request.GET:
        if request.GET['word'] !="" and request.GET['n'] !="":
            string = request.GET['word']
            n = int(request.GET['n'])
            front_len = 3
            if front_len > len(string):
                front_len = len(string)
            front = string[:front_len]
            result = ""
            for i in range(n):
                result += front
        else:
            result = None
        return render(request, 'frontTimes.html', {'result':result})
    else:
        return render(request, 'frontTimes.html')
def teen_sum(request):
    if request.GET:
        if request.GET['c'] !="" and request.GET['b'] !="" and request.GET['a'] !="":
            numbers = [int(request.GET['a']), int(request.GET['b']), int(request.GET['c'])]
            total = 0
            for number in numbers:
                if number <= 12:
                    total += number
        else:
            total = None
        return render(request, 'teenSum.html', {'total':total})
    else:
        return render(request, 'teenSum.html')
def xyz_there(request):
    if request.GET:
        if request.GET['string'] !="":
            s = request.GET['string']
            result = False
            if s[:3] == "xyz":
                result = True
            for i in range(1, len(s) - 2):
                if s[i-1] != '.' and s[i:i+3] == "xyz":
                    result = True
        else:
            result = None
        return render(request, 'xyzThere.html', {'result':result})
    else:
        return render(request, 'xyzThere.html')
def centered_average(request):
    if request.GET:
        if request.GET['array'] !="":
            array = request.GET['array'].split()
            n = len(array)
            if n % 2 == 1:
                result = array[n // 2]
            else:
                mid1 = int(array[n // 2 - 1])
                mid2 = int(array[n // 2])
                result = ((mid1 + mid2) / 2)
        else:
            result = None
        return render(request, 'centeredAverage.html', {'result':result})
    else:
        return render(request, 'centeredAverage.html')