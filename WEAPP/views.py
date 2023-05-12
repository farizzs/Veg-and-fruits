from django.shortcuts import render, redirect
from WEAPP.models import martdb, productdb, contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def indpage(req):
    return render(req,'index.html')

def addpage(req):
    return render(req,'add_category.html')

def savecategory(req):
    if req.method=='POST':
        na = req.POST.get('name')
        dcs = req.POST.get('description')
        img = req.FILES['image']
        obj = martdb(Name=na, Description=dcs, Image=img)
        obj.save()
        return redirect(addpage)

def displaypage(req):
    data = martdb.objects.all()
    return render(req, "display_category.html", {'data': data})

def editpage(req, dataid):
    data = martdb.objects.get(id=dataid)
    print(data)
    return render(req,"edit_category.html", {'data':data})

def deletepage(req, dataid):
    data = martdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaypage)

def updatepage(req, dataid):
    if req.method=='POST':
        na = req.POST.get('name')
        dcs = req.POST.get('description')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)

        except MultiValueDictKeyError:
            file = martdb.objects.get(id=dataid).image
        martdb.objects.filter(id=dataid).update(Name=na, Description=dcs, Image=file)
        return redirect(displaypage)

def addpro(req):
    data = martdb.objects.all()
    return render(req,'add_product.html', {'data':data})

def savepro(req):
    if req.method=="POST":

        pd = req.POST.get('Product')
        ct = req.POST.get('Category')
        pr = req.POST.get('Price')
        qu = req.POST.get('Quantity')
        ds = req.POST.get('Description')
        img = req.FILES['Image']
        obj = productdb(Product=pd, Category=ct, Price=pr, Quantity=qu, Description=ds, Image=img)
        obj.save()
        return redirect(addpro)

def displaypro(req):
    data = productdb.objects.all()
    return render(req, "display_product.html", {'data': data})

def editpro(req, dataid):
    data = productdb.objects.get(id=dataid)
    category_data = martdb.objects.all()
    return render(req,"edit_product.html", {'data':data,'category_data':category_data})

def deletepro(req, dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaypro)

def updatepro(req, dataid):
    if req.method=='POST':
        pd = req.POST.get('Product')
        ct = req.POST.get('Category')
        pr = req.POST.get('Price')
        qu = req.POST.get('Quantity')
        ds = req.POST.get('Description')
        try:
            img = req.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)

        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).image
        productdb.objects.filter(id=dataid).update(Product=pd, Category=ct, Price=pr, Quantity=qu, Description=ds, Image=file)
        return redirect(displaypro)

def loginpage(req):
    return render(req,'admin_login.html')

def adminlogin(req):
    if req.method=="POST":
        username_r = req.POST.get('username')
        password_r = req.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(req,user)
                req.session['username']=username_r
                req.session['password']=password_r
                return redirect(indpage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)

def adminlogout(req):
    del req.session['username']
    del req.session['password']
    return redirect(loginpage)

def displaycon(req):
    data = contactdb.objects.all()
    return render(req, "display_contact.html", {'data': data})


def deletecontact(req, dataid):
    data = contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycon)