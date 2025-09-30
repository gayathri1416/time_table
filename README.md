# Ex03 Time Table
# Date:26.09.2025
# AIM
To write a html webpage page to display your slot timetable.

# ALGORITHM
## STEP 1
Create a Django-admin Interface.

## STEP 2
Create a static folder and inert HTML code.

## STEP 3
Create a simple table using `<table>` tag in html.

## STEP 4
Add header row using `<th>` tag.

## STEP 5
Add your timetable using `<td>` tag.

## STEP 6
Execute the program using runserver command.

# PROGRAM
```
views.py:

from django.shortcuts import render
from django.http import HttpResponse
def project12(request):
    return render(request,'timetable.html') 

urls.py:

from django.contrib import admin
from django.urls import path
from myapp.views import project12

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',project12),
]

html code:

<html>
    <head>
    <title> 
        Timetable
    </title>
    </head>
    <body> 
        {% load static %}
        <img src="{% static 'logo.png' %}" alt="college logo" style="display:block; margin-left:auto; margin-right:auto;width:50%;height:auto;">
        <h1><center>SLOT TIME TABLE - GAYATHRI C (25009125)</center></h1><table border="1px" cellpadding="20px" cellspacing="4px" align="center" style="font-size:large;background-color: rgb(143, 7, 143);text-align: center;" <caption="">
        <tbody><tr style="background-color: cornsilk;font-size:x-large;">
                <th>DAY/PERIOD </th>
                <th>8:00-10:00</th>
                 <th>10:00-12:00</th>
                <th>12:00-1:00</th>
                <th>1:00-3:00</th>
                <th>3:00-5:00</th>
            </tr>
            <tr style="font-size: x-large;">
                <th style="background-color: cornsilk;">Monday</th>
                <td style="color: aliceblue;"><b>FREE</b></td>
                <td style="color: aliceblue;"><b>Web</b></td>
                <td rowspan="6" style=" writing-mode:vertical-rl;font-size: xx-large;text-orientation:upright;letter-spacing: 1cm;"><b>LUNCH</b> </td>
                <td style="color: aliceblue;"><b>FREE</b></td>
                <td style="color: aliceblue;"><b>Python</b></td>
            </tr>
            <tr style="font-size:x-large;">
                <th style="background-color:cornsilk;">Tuesday</th>
                <td style="color: aliceblue;"><b>Web</b></td>
                <td style="color: aliceblue;"><b>ML</b></td>
                <td style="color: aliceblue;"><b>Web</b></td>
                <td style="color: aliceblue;"><b>FREE</b></td>
            </tr>
            <tr style="font-size:x-large;">
                <th style="background-color: cornsilk;">Wednesday</th>
                <td style="color: aliceblue;" rowspan="2"><b>ML</b></td>
                <td style="color: aliceblue;" rowspan="2"><b>Python</b></td>
                <td style="color: aliceblue;"><b>Mentor Meet</b></td>
                <td style="color: aliceblue;"><b>ML</b></td>
            </tr>
            <tr style="font-size:x-large;">
                <th style="background-color: cornsilk;">Thursday</th>
                <td colspan="2" style="color: aliceblue;"><b>FREE</b></td>
            </tr>
            <tr style="font-size:x-large;">
                <th style="background-color: cornsilk;">Friday</th>
                <td style="color: aliceblue;"><b>Python</b></td>   
                <td style="color: aliceblue;"><b>FREE</b></td>
                <td style="color: aliceblue;"><b>Web</b></td>
                <td style="color: aliceblue;"><b>FREE</b></td>
                </tr>
                <tr style="font-size: x-large;">
                    <th style="background-color: cornsilk;">Saturday</th>
                    <td style="color: aliceblue;"><b>Web</b></td>
                    <td style="color: aliceblue;"><b>ML</b></td>
                    <td style="color: aliceblue;"><b>FREE</b></td>
                    <td style="color: aliceblue;"><b>Python</b></td>
                </tr>
        </tbody></table>
        <table border="1px" cellpadding="20px" cellspacing="4px" align="center" style="margin-top :50px;background-color: rgba(255, 228, 188, 0.755);" <tr="">
        <tbody><tr><th style="font-size:x-large;background-color:rgb(214, 8, 8);">S.NO</th>
        <th style="font-size:x-large;background-color:rgb(214, 8, 8);">SUBJECT CODE</th>
        <th style="font-size:x-large;background-color:rgb(214, 8, 8);">SUBJECT NAME</th>
        </tr>
        <tr style="font-size: x-large;">
            <td style="background-color:rgb(214, 8, 8);">1.</td>
            <td>19AI414</td>
            <td>Fundamentals Of Web Application Development(Web) </td>
        </tr>
        <tr style="font-size: x-large;">
            <td style="background-color:rgb(214, 8, 8);">2.</td>
            <td>19AI410</td>
            <td>Machine Learning (ML)</td>
        </tr>
        <tr style="font-size: x-large;">
            <td style="background-color:rgb(214, 8, 8);">3.</td>
            <td>19AI301</td>
            <td>Python</td>
        </tr>    
        </tbody></table>
</body></html>

```
# OUTPUT
![alt text](<Screenshot 2025-09-30 085538.png>)

# RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
