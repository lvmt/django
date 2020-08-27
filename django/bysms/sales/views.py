from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def listorders(request):
    cmd = '''
    <div> this is test 
        <br>
        <h1> this is a title </h1>
        <p style="color:green; font:bold"> guss what i am </p>
    </div>
    '''
    return HttpResponse(cmd)


def people(request):
    return HttpResponse('<p style="color: green"> list all people</p>')


def helloworld(request):
    return HttpResponse('<p style="font:bold; color:orange"> hello world, lvmengting</p>')