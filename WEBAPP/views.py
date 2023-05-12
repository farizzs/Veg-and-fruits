from django.shortcuts import render, redirect
from WEAPP.models import martdb, productdb, contactdb
from WEBAPP.models import Signupdb

def homepage(req):
    data = martdb.objects.all()
    return render(req,'home.html', {'data':data})

def aboutpage(req):
    data = martdb.objects.all()
    return render(req,'about.html', {'data':data})

def contactpage(req):
    data = martdb.objects.all()
    return render(req,'contact.html', {'data':data})

def shoppage(req, itemcatg):
    data = martdb.objects.all()
    products = productdb.objects.filter(Category=itemcatg)
    return render(req,'shop.html', {'products': products, 'data':data})

def singlepro(req,dataid):
    data = martdb.objects.all()
    products = productdb.objects.get(id=dataid)
    return render(req,'single_product.html',{'data':data,'products':products})

def userlog(req):
    return render(req,'user_login.html')


def saveuser(req):
    if req.method == 'POST':
        un = req.POST.get('Username')
        em = req.POST.get('Email')
        pas = req.POST.get('Password')
        con = req.POST.get('Confirm_password')
        obj = Signupdb(username=un, emailid=em, password=pas, confirm_password=con)
        obj.save()
        return redirect(userlog)

def customerlogin(req):
    if req.method == 'POST':
        username_r = req.POST.get("USERNAME")
        password_r = req.POST.get("PASSWORD")
        if Signupdb.objects.filter(username=username_r, password=password_r).exists():
            req.session['USERNAME']=username_r
            req.session['PASSWORD']=password_r

            return redirect(homepage)

        else:
            return redirect(userlog)

    return redirect(userlog)

def savecontact(req):
    if req.method == 'POST':
        na = req.POST.get('yname')
        em = req.POST.get('yemail')
        sub = req.POST.get('ysubject')
        msg = req.POST.get('ymessage')
        obj = contactdb(Name=na, Email=em, Subject=sub, Message=msg)
        obj.save()
        return redirect(contactpage)
def logout(req):
    del req.session['USERNAME']
    del req.session['PASSWORD']
    return redirect(userlog)