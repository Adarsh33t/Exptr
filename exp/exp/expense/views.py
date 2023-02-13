from shutil import register_unpack_format
from unicodedata import name
from django.shortcuts import redirect, render,HttpResponse
from markupsafe import re
from matplotlib.style import context
from platformdirs import user_cache_dir

from django.contrib import messages
from .models import *

from django.contrib.auth.models import User



# Create your views here.
def home(request):
    
      profile=Profile.objects.filter().first()
      expenses=Expense.objects.filter()
      if request.method== 'POST':
          text=request.POST.get('text')
          amount=request.POST.get('amount')
          expense_type=request.POST.get('expense_type')
          expenses[0].save()
          if(expense_type=='Positive'):
              profile.balance+= float(amount)
          else:
              profile.expenses+=float(amount)
              profile.balance-=float(amount)
          profile.save()
          return redirect('/')
      context={'profile':profile,'expenses':expenses}
      return render(request,'home.html',context)
    
def signup(request):
    if request.method == 'POST':
        username =request.POST['username']
        fname =request.POST['fname']
        lname= request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']





        myuser =User.objects.create_user(username,email,pass1)
        myuser.firstname=fname
        myuser.lastname=lname
        myuser.save()
        messages.success(request,"your account has been created")
        return redirect('home')

    else:
        return HttpResponse('404 - Not Found')