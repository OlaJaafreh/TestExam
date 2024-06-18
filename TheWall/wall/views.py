from django.shortcuts import render ,redirect
from .models import Messages , Users , Comments
from django.contrib import messages
from datetime import datetime, timedelta
from django.utils import timezone
import bcrypt

def index(request):
    return render(request,"login.html")

def index1(request):
    messages =reversed(Messages.objects.all())
    user = Users.objects.get(id =request.session['userid'])
    return render(request,"index.html",{'messagess':messages,'user':user})

def creat(request):
        
    errors = Users.objects.basic_validator(request.POST)
    if len(errors) > 0:
        messages.error(request, 'Registration failed.')
        return render(request,'login.html', {'errors': errors})
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        Users.objects.create(first_name=first_name,last_name=last_name,email=email,password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode())
        messages.success(request, 'Registration successful. You can now log in.')
        return render(request ,"login.html")

def Login(request):
    email = request.POST.get('emailLog')
    password = request.POST.get('pass')
    user = Users.objects.filter(email=email)  
    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(password.encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect("index1")
        else:
            messages.error(request, 'Incorrect Password')
    else:
        messages.error(request, 'Email not found')
    return redirect('index')
    
    

def Logout(request):
    del request.session['userid']
    return redirect("/")
        


def addMessage(request,U_id):
    message = request.POST['themessage']
    Messages.objects.create(message=message,user_id=Users.objects.get(id=U_id))
    
    return redirect("index1")

def addComment(request,U_id,M_id):
    comment = request.POST['thecomment']
    Comments.objects.create(comment=comment,user_id=Users.objects.get(id=U_id),message_id=Messages.objects.get(id=M_id))
    
    return redirect("index1")

def addUser(request):
    user = Users.objects.create(first_name='Ola',last_name ='jaafreh',email='jfkfddfde',password ='jdkikf')
    users = Users.objects.all()
    return redirect('index1')


def delete(request,M_id):
    message = Messages.objects.get(id=M_id)
    if timezone.now() - message.created_at <= timedelta(minutes=30):
        message.delete()
        messages.success(request, "Message deleted successfully.")
    else:
        messages.warning(request,'you can only delete messages within 30 minutes of posting')
    return redirect('index1')