from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def savedata(request):
    # Name=request.POST['name']
    # Email=request.POST['email']
    # Contact=request.POST['contact']
    # City=request.POST['city']
    # Password=request.POST['pswd']
    # # print(Name,Email,Contact,City,Password)
    # response=render(request,'login.html')
    # response.set_cookie("Name",Name)
    # response.set_cookie("Email",Email)
    # response.set_cookie("Contact",Contact)
    # response.set_cookie("City",City)
    # response.set_cookie("Password",Password)
    # return response
    fname=request.POST['name']
    email=request.POST['email']
    Contact=request.POST['contact']
    City=request.POST['city']
    Password=request.POST['password']
    request.session['name']=fname
    request.session['email']=email
    request.session['contact']=Contact
    request.session['city']=City
    request.session['password']=Password
    return render(request,'login.html')


def login1(request):
    email=request.POST['email']
    password=request.POST['password']
    print(email)
    print(password)
    email_id = request.session['email']
    pwd = request.session['password']


    if email==email_id and password==pwd:
        name=request.session['name']
        return render(request,'dashboard.html',{'data':name})
# def logout(request):
#     deletedata=render(request,'home.html')
def logindata(request):
    del request.session['email']
    del request.session['name']
    request.session.flush()
    return render(request,'home.html')

def home(request):
   #  if 'name' in request.session:
   #      name=request.session['name']
   #      return render(request,'home.html',{'data':name})
   #  else:
   #      return render(request,'home.html')
    try:
         data=request.session['name']
         request.session.modified=True
         return render(request,'home.html',{'data':data})
    except:
         return render(request,'home.html')
def about(request):
   #   if 'name' in request.session:
   #      name=request.session['name']
   #      return render(request,'about.html',{'data':name})
   #   else:
   #      return render(request,'about.html')
     try:
         data=request.session['name']
         request.session.modified=True
         return render(request,'about.html',{'data':data})
     except:
         return render(request,'about.html')
   
def contact(request):
   #   if 'name' in request.session:
   #      name=request.session['name']
   #      return render(request,'contact.html',{'data':name})
   #   else:
   #      return render(request,'contact.html')
    try:
         data=request.session['name']
         request.session.modified=True
         return render(request,'contact.html',{'data':data})
    except:
         return render(request,'contact.html')
    
def services(request):
   #   if 'name' in request.session:
   #      name=request.session['name']
   #      return render(request,'services.html',{'data':name})
   #   else:
   #      return render(request,'services.html')
    try:
         data=request.session['name']
         request.session.modified=True
         return render(request,'services.html',{'data':data})
    except:
         return render(request,'services.html')
    
def login(request):
     if 'name' in request.session:
        name=request.session['name']
        return render(request,'login.html',{'data':name})
     else:
        return render(request,'login.html')
    
def registration(request):
     if 'name' in request.session:
        name=request.session['name']
        return render(request,'registration.html',{'data':name})
     else:
        return render(request,'registration.html')
    
def dashboard(request):
     if 'name' in request.session:
        name=request.session['name']
        return render(request,'dashboard.html',{'data':name})
     else:
        return render(request,'dashboard.html')
     
def datadelete(request):
    request.session.flush()
    return render(request,'home.html')
def get(request):
    if 'name' in request.session:
        request.session.modified=True
        name=request.session['name']

        return render(request,'home.html',{"data":name})
    else:
        return HttpResponse("<h1>Your session is expired</h1>")
