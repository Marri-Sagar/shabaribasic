from django.shortcuts import render

# Create your views here.
def basic(request):
    return render(request,'hai.html')

def final(request):
    uname=request.POST.get('u1')
    pwd=request.POST.get('p1')
    return render(request,'final.html',{"uname":uname,"pd":pwd})
