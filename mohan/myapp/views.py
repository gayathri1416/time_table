from django.shortcuts import render
from django.http import HttpResponse
def project12(request):
    return render(request,'timetable.html')


