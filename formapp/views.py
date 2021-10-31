from django.http.response import HttpResponseBadRequest
from django.shortcuts import redirect, render
from . import models
from django.contrib  import messages


# Create your views here.
def index(request):
    if request.method=="POST":
        name = request.POST['name']
        reg = request.POST['reg']
        phone = request.POST['phone']
        branch =  request.POST['branch']
        email =  request.POST['email']
        image = request.FILES.get('images')

        if len(phone)!=10:
            messages.info(request, "Phone number is Invalid")
            return redirect('index')
        elif image is None:
            messages.info(request,"image is not found")
            return  redirect('index')
        else:
            data = models.Data(name=name,reg=reg,phone=phone,branch=branch,email=email,image=image)
            data.save()
            return redirect('success')
    return render(request,'index.html')

def success(request):
    return render(request,'success.html')