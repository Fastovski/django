
from unicodedata import name
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Products, Supplier, ProductVote, ExpertVoted
from kursach.forms import RegForm, LogForm, ExpertForm, searchpr



class da():
    def regform():pass
    def logform():pass
    def searchpr():pass

class da2(da):
    def regform(self):  
        form=RegForm()
        return form

class da3(da):
    def logform(self):  
        form=LogForm()
        return form
        
class da4(da):
    def searchpr(self):  
        form=searchpr()
        return form

def index(request):
    username = request.user.username
    usernamevote = ExpertVoted.objects.filter(user = username)
    data ={'username':username,'usernamevote':usernamevote}
    return render(request, 'index.html', context=data)
    
def register(request):
    # form = RegForm ()
    form2 = da2()
    form = form2.regform()
    if request.method == 'POST':
        username = request.POST ['username']
        email = request.POST ['email']
        password = request.POST ['password']
        password1 = request.POST ['password1']

        if password == password1:
            if User.objects.filter(email = email).exists():         
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                return redirect('register')
            else: 
                user = User.objects.create_user(username=username, email=email,password=password,)
                user.save()
                is_voted = False
                vote = ExpertVoted.objects.create(user=username, is_voted=is_voted)
                vote.save()
                return redirect ('login')
        else:
            messages.info (request, 'Password not the same')
            return redirect ('register')
    else:
        return render (request, 'register.html',{'form':form})
        

def login(request):
    # form = LogForm ()
    form3 = da3()
    form = form3.logform()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            
            return redirect('login')
    else:
        return render (request, 'login.html', {'form':form})

def logout(request):
    auth.logout(request)
    return redirect('/')

def products(request):
    sp = Supplier.objects.all()
    pr = Products.objects.all()
    data ={'pr':pr,'sp':sp}
    return render (request, 'product.html', data)

def ordername(request):
    sp = Supplier.objects.all()
    pr = Products.objects.order_by('name')
    data ={'pr':pr,'sp':sp}
    return render (request, 'product.html', data)

def ordercost(request):
    sp = Supplier.objects.all()
    pr = Products.objects.order_by('cost')
    data ={'pr':pr,'sp':sp}
    return render (request, 'product.html', data)

def ordersupplier(request):
    sp = Supplier.objects.order_by('name')
    pr = Products.objects.all()
    data ={'pr':pr,'sp':sp}
    return render (request, 'product.html', data)

def infosupplier(request): 
    return render (request, 'product.html')

def search (request):
    
    return render (request, 'search.html')

def searchprod(request):
    form4 = da4()
    form = form4.searchpr()
    if request.method == 'POST':
        name = request.POST['pr']
        prods = Products.objects.filter(name=name)
        sp = Supplier.objects.all()
        sp2 = list()
        for i in prods:
            for j in sp:
                if(i.supplier.name == j.name):
                    sp2.append(j)
        data = {"sp":sp2, "pr":prods}
        return render(request, 'search.html', context=data)
    else: 
        form = searchpr()
        data = {"form":form}
        return render(request, 'searchprod.html', context=data)

def expertmark(request):
    if request.method == 'POST':
        product1mark = request.POST['product1mark']
        product2mark = request.POST['product2mark']
        product3mark = request.POST['product3mark']
        products = ProductVote.objects.create(product1mark=product1mark, product2mark=product2mark,product3mark=product3mark,)
        products.save()
        user = request.user.username
        vote = ExpertVoted.objects.get(user=user)
        vote.is_voted = True
        vote.save()
        return redirect('/')
    else:
        form = ExpertForm()
        return render (request, 'expertmark.html', {'form':form})

def expertresult(request):
    a = 0
    result1 = 0
    result2 = 0
    result3 = 0
    products = ProductVote.objects.all()
    pr = Products.objects.all()
    for product in products:
        result1 += product.product1mark
        result2 += product.product2mark
        result3 += product.product3mark
        a += 1
    result1 = result1/a
    result2 = result2/a
    result3 = result3/a
    if result1 > result2 and result1 > result3:
        prname = pr[0].name
        result = result1
    elif result2 > result1 and result2 >result3:
        prname = pr[1].name
        result = result2
    else:
        prname = pr[2].name
        result = result3
    data ={'prname':prname,'result':result}
    return render (request, 'result.html', data)