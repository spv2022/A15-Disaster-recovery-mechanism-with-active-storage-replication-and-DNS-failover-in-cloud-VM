from django.shortcuts import render
from django.http import HttpResponse, request, HttpResponseRedirect
from monthlych.models import Register
import socket
import subprocess


# Create your views here.
def home(request):
    hostname=socket.gethostname()
    hip = subprocess.run(['curl','ifconfig.me'],stdout=subprocess.PIPE)
    regdata = 'Host name : {hostname} \n Host Ip :{hostip} '.format(hostname=hostname,hostip='{a} ( {b} )'.format(a=hip.stdout,b=socket.gethostbyname(hostname)))
    if request.method =='POST':
        f_data=request.POST
        name= f_data['name']
        email=f_data['email']
        college= f_data['college']
        contact = f_data['no']
        loc = f_data['loc']
        #hresp = "<p>"+name+ email +college+contact+loc+ "<p>"
        reg = Register.objects.create(name= name,mailid=email,college= college,contact=contact,loc=loc)
        #return HttpResponse(hresp)
        return render(request,'monthlych/index.html',{'regdata':regdata,'data':'you have registered your information, please check the admin portal'})
    #return HttpResponse("<h1>iam inside chal</h1>")
    elif request.method =='GET':
        
        return render(request,'monthlych/index.html',{'regdata':regdata})

def regis(request):
    return render(request,'monthlych/register.html')
