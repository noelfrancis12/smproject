from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.conf import settings
from smapp.models import Details
# Create your views here.
def home(request):
    return render(request,"home.html")
def login1(request):
 if request.method == 'POST':
    username=request.POST['username']
    password=request.POST['password']
    user = auth.authenticate(username=username, password=password) 
    #request.session["uid"]=user.id#session method part
    if user is not None:
        if user.is_staff:
            login(request,user)
            messages.success(request,'Welcome Admin...')
            return redirect('adminprofile')
        else:
            login(request,user)
            auth.login(request,user)
            messages.success(request,'Welcome Back...')
            return redirect('userprofile')
        
    else:
        messages.info(request,'Invalid Username or Password. Try again.')
        return redirect('home')
 else:
     return redirect('home')
@login_required(login_url='login1')
def logout(request):
    #if request.user.is_authenticated:(is authenticated method part)
    #request.session["uid"] = ""#session method part
    auth.logout(request)
    return redirect('home')
@login_required(login_url='login1')   
def adminprofile(request):
    
    u=Details.objects.all
    
    
    return render(request,'admin_profile.html',{'usrkey':u})
def signup(request):
    return render(request,'signup.html') 
def signupdb(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name') 
        username=request.POST.get('username')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        address=request.POST.get('address')
        email=request.POST.get('email')
        number=request.POST.get('number')
        age=request.POST.get('age')
        image=request.FILES.get('image')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username already exists !!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
                user.save()
                u=User.objects.get(id=user.id)

                
                member=Details(address=address,number=number,age=age,image=image,userc=u)
                member.save()

                

                return redirect('/')
        else:
            messages.info(request,'Password does match !!!')
            return redirect('signup')
    else:
        return render(request,'signup.html')
@login_required(login_url='login1')
def userprofile(request):
    # if not request.user.is_staff:
    #     return redirect('/')
    ucuser=request.user.id
    use=Details.objects.get(userc_id=ucuser)
   
    return render(request,'user_profile.html',{'usrkey':use})
def editpage(request):
    
    customer=Details.objects.get(userc=request.user)
    context={'usrkey': customer}
    return render(request,'accountedit.html',context)


def editdetails(request,pk):
    
    if request.method=='POST':
        
        customer=Details.objects.get(id=pk)
        user_id=customer.userc.id
        user=User.objects.get(id=user_id)
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        user.username=request.POST.get('username')
        user.email=request.POST.get('email')
       
        customer.age=request.POST.get('age')
        customer.number=request.POST.get('number')
        customer.address=request.POST.get('address')
        old=customer.image
        new=request.FILES.get('files')
        if old != None and new==None:
            customer.image=old
        else:
            customer.image=new 
          
     

        customer.save()
        user.save()
        messages.success(request,'Profile Updated')
        
        
        return redirect('userprofile')
@login_required(login_url='login1')
def deleteu(request,pk):
    emp=Details.objects.get(id=pk)
    emp.delete()
    return redirect('adminprofile')    