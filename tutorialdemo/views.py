from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Contactform,productform,studentform,DocumentForm
from .models import Student,Document
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.
def home(request):
    # return HttpResponse("Hello Django")
    return render(request,"home.html")

def footer(req):
    # return HttpResponse("Footer page")
    return render(req,"footer.html")

def users(req):
    uname="Sivanantham"
    title=f"user {uname}"
    role="user"
    names=["html","css","js","python","django"]
    return render(req,"user.html",context={'name':uname,'title':title,'role':role,'language':names})

def contact(req):
    if req.method=='POST':
        form=Contactform(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form=Contactform()

    return render(req,'contact.html',{'form':form})    

def product_create(req):
    if req.method=="POST":
        form=productform(req.POST)

        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form=productform()

    return render(req,"product.html",{"form":form})

def stu_create(req):
    if req.method=='POST':
        form=studentform(req.POST)

        if form.is_valid():
            form.save()
            messages.success(req,"Student data created successfully!!")
            return redirect("/stu/")
    else:
        form=studentform()
    return render(req,"stu.html",{"form":form})


def student_list(req):
    students=Student.objects.all()

    paginator=Paginator(students,2)

    page_number=req.GET.get("page")
    student_page=paginator.get_page(page_number)
    return render(req,"stu.html",{"students":student_page})

def stu_delete(req,id):
    stu=Student.objects.get(id=id)
    stu.delete()
    return redirect('/stu/')

def update_data(req,id):
    selected_data=Student.objects.get(id=id)

    context={
        "student_form":studentform(instance=selected_data)
    }

    if req.method=='POST':
        data=studentform(req.POST,instance=selected_data)
        if data.is_valid():
            data.save()
            return redirect("/list/")

    return render(req,"form.html",context)

def file_upload(req):
    if req.method=="POST":
        form=DocumentForm(req.POST,req.FILES)

        if form.is_valid():
            form.save()
            return redirect("/upload/")
    else:
            form=DocumentForm()

    return render(req,"upload.html",{"form":form})

def set_session(req):
    req.session["username"]="siva"
    req.session["role"]="student"
    return HttpResponse("Session data saved")

def get_session(req):
    username=req.session.get("username")
    role=req.session.get("role")
    return HttpResponse(f"Username: {username} <br> Role: {role}")

def delete_session(req):
    req.session.flush()
    return HttpResponse("Session removed")

def set_cookie(req):
    response =HttpResponse("Cookie saved")

    response.set_cookie(
        "username","siva",max_age=2500
    )

    return response

def get_cookie(req):
    username=req.COOKIES.get("username")
    return HttpResponse(f"Username {username}")

def delete_cookie(req):
    response=HttpResponse("Cookie deleted")

    response.delete_cookie("username")
    return response