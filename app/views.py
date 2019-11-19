from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *
from random import randint
from .utils import *

# Create your views here.
def RegisterPage(request):
    return render(request,"app/register.html")

def LoginPage(request):
    return render(request,"app/login.html")

def registeruser(request):
    try:
        if request.POST['role']=="admin":
            role = request.POST['role']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['pass']
            cpassword = request.POST['cpass']
            user = User.objects.filter(email=email)
            if user:
                message = "User doesnot get"
                return render(request,"app/register.html",{'message':message})
            else:
                if password==cpassword:
                    otp = randint(100000,9999999)

                    newuser = User.objects.create(role=role,email=email,password=password,otp=otp)
                    newadmin = Admin.objects.create(user_id=newuser,fname=fname,lname=lname)
                    #subject = "Admin login verification"
                    #sendmail(subject,'mailtemplate',email,{'name':fname,'otp':otp})
                    return HttpResponseRedirect(reverse('homepage'))
                else:
                    message = "Password doesnot match"
                    return render(request,"app/register.html",{'message':message})
           
        else:
            role = request.POST['role']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['pass']
            cpassword = request.POST['cpass']
            user = User.objects.filter(email=email)
            if user:
                if password==cpassword:
                    otp = randint(100000,999999)

                    newuser = User.objects.create(role=role,email=email,password=password,otp=otp)
                    newadmin = Admin.objects.create(user_id=newuser,fname=fname,lname=lname)
                    #subject = "Employee login verification"
                    #sendmail(subject,'mailtemplate',email,{'name':fname,'otp':otp})
                    return HttpResponseRedirect(reverse('homepage'))
                else:
                    message = "Password does not match"
                    return render(request,"app/register.html",{'message':message})
            else:
                message = "User doesnot get"
                return render(request,"app/register.html",{'message':message})
    

    except User.DoesNotExist:
        message = "User doesnot Exist"
        return render(request,"app/register.html",{'message':message})

def HomePage(request):
    if 'email' in request.session and 'role' in request.session:
        if request.session['role'] == 'admin':
            all_admin = Admin.objects.all()
            all_employee = employee.objects.all()
            return render(request,"app/homepage.html",{'all_admin':all_admin,'all_employee':all_employee})
        else:
            all_employee = employee.objects.all()
            return render(request, 'app/homepage.html', {'all_employee': all_employee})
    else:
        return HttpResponseRedirect(reverse('loginpage'))
    return render(request,"app/homepage.html")

def Loginuser(request):
    if request.POST['role'] == 'admin':
        email = request.POST['email']
        password = request.POST['pass']

        user = User.objects.filter(email=email)
        print("<--------user----------->",user)
        if user[0]:
            if user[0].password==password and user[0].role=='admin':
            #    # if (user[0].is_verified == False):
            #     #     return HttpResponseRedirect(reverse('otp'))
            #     else:
                    admin = Admin.objects.filter(user_id=user[0])
                    request.session['email'] = user[0].email
                    request.session['role'] = user[0].role
                    request.session['id'] = user[0].id

                    return HttpResponseRedirect(reverse('homepage'))
            else:
                message = "password is not correct or user is not defined"
                return render(request,"app/login.html",{'message':message})

        else:
            message = "user doesn't exist"
            return render(request,"app/login.html",{'message':message})

    if request.POST['role'] == 'employee':
        email = request.POST['email']
        password = request.POST['pass']

        user = User.objects.filter(email=email)
        prin(user)
        if user[0]:
            if user[0].password==password and user[0].role=='employee':
                # if (user[0].is_verified == False):
                #     return HttpResponseRedirect(reverse('otp'))
                # else:
                    admin = Admin.objects.filter(user_id=user[0])
                    request.session['email'] = user[0].email
                    request.session['fname'] = user[0].fname
                    request.session['role'] = user[0].role
                    request.session['id'] = user[0].id

                    return HttpResponseRedirect(reverse('homepage'))
            else:
                message = "password is not correct or user is not defined"
                return render(request,"app/login.html",{'message':message})

        else:
            message = "user doesn't exist"
            return render(request,"app/login.html",{'message':message})

def otp(request):
    return render(request,'app/otp.html')            

def user_verification(request):
    email = request.session['email']
    otp = request.session['otp']

    user = User.objects.get(otp=otp)
    if user:
        if str(user.otp) == otp:
            user.is_verified = True
            user.save()
            if user.role == 'Admin':
                return render(request,'app/admin.html')
            else:
                return render(request,'app/employee.html')
        else:
            return render(request,'app/login.html')
    else:
        return render(request,'app/register.html')                    
        

def IndexPage(request):
    return render(request,"app/index.html")

def logout(request):
    del request.session['email']
    del request.session['role']
    return HttpResponseRedirect(reverse('loginpage'))

