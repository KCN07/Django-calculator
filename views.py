
from django.shortcuts import render
def home(request):
    if request.method == "POST":
        val1 = request.POST['val1']
        val2 = request.POST['val2']
        sign = request.POST['sign']
        y = eval(val1 + sign + val2)
        return render(request, 'result.html', context={'y': y})
    return render(request, 'calculo.html')
