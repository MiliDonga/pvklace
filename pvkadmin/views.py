import datetime
import os
from django.conf import settings
from django.contrib.auth.models import User

from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from pvkadmin.models import category, product, home_banner, team, inquiry, order, about_banner, contact, product_photo


# Create your views here.
def admin_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username != "" and password != "":
            user = authenticate(username=username, password=password)
            if user is not None:
                request.session["id"] = user.id
                login(request,user)
                return redirect("dashboard/")
            else:
                return render(request, "admin_login.html", {"error": "Username or password is incorrect."})
        else:
            return render(request, "admin_login.html",{"error":"Please fill all the field."})
    return render(request,"admin_login.html")

@login_required(login_url="/admin-side/")
def admin_index(request):
    inq = inquiry.objects.all().order_by('created_at').values()
    ord = order.objects.all().order_by('created_at').values()
    con = contact.objects.all().order_by('created_at').values()
    quantity = 0
    amount = 0
    for item in ord:
        amount += item['amount']
    for item in ord:
        quantity += item['quantity']
    data = {
        "inquiry": inq,
        "contact":con,
        "order_count": len(ord),
        "revenue": amount,
        "average": round(amount/quantity, 2),
        'quantity':quantity
    }
    return render(request,"admin_index.html",data)

@login_required(login_url="/admin-side/")
def admin_category(request):
    cat = category.objects.all().values()
    return render(request,"admin_category.html",{'category':cat})

@login_required(login_url="/admin-side/")
def admin_home_banner(request):
    home = home_banner.objects.all().values()

    data = {
        'banner_1': {'image':home[0]['banner_image'],
                     'link':home[0]['link']
                     },
        'banner_2': {'image':home[1]['banner_image'],
                     'link':home[1]['link']
                     },
        'banner_3': {'image':home[2]['banner_image'],
                     'link':home[2]['link']
                     },
    }
    return render(request,"admin_home-banner-images.html",data)

@login_required(login_url="/admin-side/")
def admin_product(request):
    pro = product.objects.all().values()
    cat = category.objects.all().filter(is_active=True).values()
    categories = {}
    for item in pro:
        id = item['category']
        item['category'] = category.objects.get(id=id).category_name
    for item in cat:
        categories[item['id']] = item['category_name']
    data = {
        'category': categories,
        'product': pro
    }
    return render(request,"admin_products.html", data)

@login_required(login_url="/admin-side/")
def admin_team(request):
    tea = team.objects.all().values()
    return render(request,"admin_team.html",{'team':tea})

@login_required(login_url="/admin-side/")
def admin_about_banner(request):
    about = about_banner.objects.all().values()

    data = {
        'banner': about[0]['banner_image'],
        'slide': about[1:],
    }
    return render(request,"admin_about-us-banner-images.html",data)

@login_required(login_url="/admin-side/")
def admin_logout(request):
    request.session["id"] = ""
    logout(request)
    return redirect("/admin-side/")

@login_required(login_url="/admin-side/")
def add_category(request):
    if request.method == "POST" and request.FILES['image']:
        cat = category(category_image=request.FILES['image'], category_name=request.POST['name'])
        cat.save()
        request.session['add'] = 1
        return redirect("/admin-side/category/")

@login_required(login_url="/admin-side/")
def update_session(request):
    request.session['update'] = 0
    return HttpResponse('ok')

@login_required(login_url="/admin-side/")
def add_session(request):
    request.session['add'] = 0
    return HttpResponse('ok')

@login_required(login_url="/admin-side/")
def delete_data_session(request):
    request.session['delete_data_session'] = 0
    return HttpResponse('ok')

@login_required(login_url="/admin-side/")
def get_category_data(request):
    cat = category.objects.get(id=request.GET.get('id'))
    data = {
        'id': cat.id,
        'name': cat.category_name,
    }
    return JsonResponse({"data": data})

@login_required(login_url="/admin-side/")
def update_category(request):
    if request.method == "POST":
        if 'image' in request.FILES:
            cat = category.objects.get(id=request.POST['id'])
            path = "media/" + str(cat.category_image)
            os.remove(path)
            cat.category_image = request.FILES['image']
            cat.category_name=request.POST['name']
            cat.updated_at=datetime.datetime.now()
            cat.save()
        else:
            category.objects.filter(id=request.POST['id']).update(category_name=request.POST['name'],
                                                                  updated_at=datetime.datetime.now())

        request.session['update'] = 1
        return redirect("/admin-side/category/")

@login_required(login_url="/admin-side/")
def category_status(request):
    cat = category.objects.get(id=request.GET['id'])
    if cat.is_active:
        cat.is_active = False
        product.objects.all().filter(category=cat.id).update(is_active=False)
    else:
        cat.is_active = True
        product.objects.all().filter(category=cat.id).update(is_active=True)
    cat.updated_at = datetime.datetime.now()
    cat.save()
    request.session['update'] = 1
    return HttpResponse("OK")

@login_required(login_url="/admin-side/")
def get_product_data(request):
    pro = product.objects.get(id=request.GET.get('id'))
    photo = product_photo.objects.all().filter(product_id = request.GET.get('id')).values();
    image = []
    for item in photo:
        image.append({
            "id": item['id'],
            "image": item['image'],
            "product_id": item['product_id']
        })
    data = {
        'id': pro.id,
        'name': pro.product_name,
        'description': pro.product_description,
        'category': pro.category,
        'product_image':image,
    }
    return JsonResponse({"data": data})

@login_required(login_url="/admin-side/")
def add_product(request):

    if request.method == "POST" and request.FILES['product_image']:
        pro = product(product_image=request.FILES['product_image'],product_name=request.POST['name'],product_description=request.POST['product_description'],category=request.POST['category'])
        pro.save()
        photo = product_photo(product=pro, image=request.FILES['product_image'])
        photo.save()
        if request.FILES.getlist('file[]'):
            for data in request.FILES.getlist('file[]'):
                photo = product_photo(product=pro,image=data)
                photo.save()
        request.session['add'] = 1
        return redirect("/admin-side/product/")

@login_required(login_url="/admin-side/")
def product_status(request):
    pro = product.objects.get(id=request.GET['id'])
    if pro.is_active:
        pro.is_active = False
    else:
        pro.is_active = True
    pro.updated_at = datetime.datetime.now()
    pro.save()
    request.session['update'] = 1
    return HttpResponse("OK")

@login_required(login_url="/admin-side/")
def update_product(request):

    if request.method == "POST":
        if 'image' in request.FILES:
            pro = product.objects.get(id=request.POST.get('id'))
            path = "media/" + str(pro.product_image)
            os.remove(path)
            pro.product_image = request.FILES['image']
            pro.product_name=request.POST['name']
            pro.product_description=request.POST['product_description']
            pro.category=request.POST['category']
            pro.updated_at=datetime.datetime.now()
            pro.save()
            photo = product_photo(product=pro,image=request.FILES['image'])
            photo.save()
            if request.POST.get('delete_id') != "":
                delete_data = (request.POST.get('delete_id')).split()
                for data in delete_data:
                    photo = product_photo.objects.get(id=data)
                    path = "media/" + str(photo.image)
                    os.remove(path)
                    photo.delete()
            if request.FILES.getlist('file[]'):
                for data in request.FILES.getlist('file[]'):
                    photo = product_photo(product=pro,image=data)
                    photo.save()

        else:
            product.objects.filter(id=request.POST['id']).update(product_name=request.POST['name'],product_description=request.POST['product_description'],category=request.POST['category'],
                                                                  updated_at=datetime.datetime.now())
            if request.POST.get('delete_id') != "":
                delete_data = (request.POST.get('delete_id')).split()
                for data in delete_data:
                    photo = product_photo.objects.get(id=data)
                    path = "media/" + str(photo.image)
                    os.remove(path)
                    photo.delete()
            if request.FILES.getlist('file[]'):
                for data in request.FILES.getlist('file[]'):
                    pro = product.objects.get(id=request.POST.get('id'))
                    photo = product_photo(product=pro,image=data)
                    photo.save()

        request.session['update'] = 1
        return redirect("/admin-side/product/")

@login_required(login_url="/admin-side/")
def update_home(request):
    if request.method == "POST":
        if 'image' in request.FILES:
            home = home_banner.objects.get(id=request.POST.get('id'))
            path = "media/" + str(home.banner_image)
            os.remove(path)
            home.banner_image = request.FILES['image']
            home.link = request.POST['link']
            home.save()
        else:
            home_banner.objects.filter(id=request.POST.get('id')).update(link = request.POST['link'])
        request.session['update'] = 1
        return redirect("/admin-side/home_banner/")

@login_required(login_url="/admin-side/")
def add_team(request):
    if request.method == "POST" and request.FILES['image']:
        tea = team(member_image=request.FILES['image'],member_name=request.POST['name'])
        tea.save()
        request.session['add'] = 1
        return redirect("/admin-side/team/")

@login_required(login_url="/admin-side/")
def team_status(request):
    tea = team.objects.get(id=request.GET['id'])
    if tea.is_active:
        tea.is_active = False
    else:
        tea.is_active = True
    tea.updated_at = datetime.datetime.now()
    tea.save()
    request.session['update'] = 1
    return HttpResponse("OK")

@login_required(login_url="/admin-side/")
def update_team(request):

    if request.method == "POST":
        if 'image' in request.FILES:
            tea = team.objects.get(id=request.POST.get('id'))
            path = "media/" + str(tea.member_image)
            os.remove(path)
            tea.member_image = request.FILES['image']
            tea.member_name=request.POST['name']
            tea.updated_at=datetime.datetime.now()
            tea.save()
        else:
            team.objects.filter(id=request.POST['id']).update(member_name=request.POST['name'],
                                                                  updated_at=datetime.datetime.now())

        request.session['update'] = 1
        return redirect("/admin-side/team/")

@login_required(login_url="/admin-side/")
def get_team_data(request):
    tea = team.objects.get(id=request.GET.get('id'))
    data = {
        'id': tea.id,
        'name': tea.member_name,
    }
    return JsonResponse({"data": data})

@login_required(login_url="/admin-side/")
def team_delete(request):
    tea = team.objects.get(id=request.GET['id'])
    path = "media/" + str(tea.member_image)
    os.remove(path)
    tea.save()
    team.objects.get(id=request.GET['id']).delete()
    request.session['delete_data_session'] = 1
    return HttpResponse("OK")

@login_required(login_url="/admin-side/")
def product_delete(request):
    photo = product_photo.objects.all().filter(product_id=request.GET.get('id')).values()
    for item in photo:
        path = "media/" + str(item['image'])
        os.remove(path)
    pro = product.objects.get(id=request.GET.get('id'))
    path = "media/" + str(pro.product_image)
    os.remove(path)
    pro.delete()
    request.session['delete_data_session'] = 1
    return HttpResponse("OK")

@login_required(login_url="/admin-side/")
def category_delete(request):
    cat = category.objects.get(id=request.GET['id'])
    pro = product.objects.all().filter(category=cat.id).values()
    for item in pro:
        path = "media/" + str(item['product_image'])
        os.remove(path)
        product.objects.get(id=item['id']).delete()
    path = "media/" + str(cat.category_image)
    os.remove(path)
    cat.save()
    category.objects.get(id=request.GET['id']).delete()
    request.session['delete_data_session'] = 1
    return HttpResponse("OK")

@login_required(login_url="/admin-side/")
def update_inquiry(request):
    if request.method == 'POST':
        inq = inquiry.objects.get(id=request.POST['id'])
        inq.status = True
        inq.save()
        if order.objects.filter(inquiry_id=inq.id).exists():
            order.objects.filter(inquiry_id=inq.id).update(inquiry_id=inq.id, item_name=inq.item_name, category=inq.category,
                        amount=request.POST['amount'], quantity=request.POST['quantity'])
            return redirect("/admin-side/dashboard/")
        ord = order(inquiry_id=inq.id, item_name=inq.item_name, category=inq.category,
                    amount=request.POST['amount'], quantity=request.POST['quantity'])
        ord.save()
        return redirect("/admin-side/dashboard/")
    return redirect("/admin-side/dashboard/")

@login_required(login_url="/admin-side/")
def get_info_inquiry(request):
    inq = inquiry.objects.get(id=request.GET['id'])
    if order.objects.filter(id=inq.id).exists():
        ord = order.objects.get(inquiry_id=inq.id)
        data = {
            'id': inq.id,
            'amount': ord.amount,
            'quantity': ord.quantity,
        }
        return JsonResponse(data)
    data = {
        'id': inq.id,
        'amount': "",
        'quantity': "",
    }
    return JsonResponse(data)

@login_required(login_url="/admin-side/")
def add_about_image(request):
    if request.method == "POST" and request.FILES['image']:
        if request.POST['name'] != "":
            tea = about_banner(banner_image=request.FILES['image'],text=request.POST['name'],category="slider")
            tea.save()
        else :
            tea = about_banner(banner_image=request.FILES['image'], category="banner")
            tea.save()
        request.session['add'] = 1
        return redirect("/admin-side/about/")

@login_required(login_url="/admin-side/")
def update_about_image(request):
    if request.method == "POST":
        print(request.POST)
        if 'image' in request.FILES:
            if 'name' in request.POST:
                tea = about_banner.objects.get(id=request.POST['id'])
                path = "media/" + str(tea.banner_image)
                os.remove(path)
                tea.banner_image = request.FILES['image']
                tea.text=request.POST['name']
                tea.updated_at=datetime.datetime.now()
                tea.save()
            else:
                tea = about_banner.objects.get(id=request.POST.get('id'))
                path = "media/" + str(tea.banner_image)
                os.remove(path)
                tea.banner_image = request.FILES['image']
                tea.updated_at = datetime.datetime.now()
                tea.save()
        else:
            about_banner.objects.filter(id=request.POST['id']).update(text=request.POST['name'],
                                                                  updated_at=datetime.datetime.now())

        request.session['update'] = 1
        return redirect("/admin-side/about/")

@login_required(login_url="/admin-side/")
def delete_about_image(request):
    tea = about_banner.objects.get(id=request.GET['id'])
    path = "media/" + str(tea.banner_image)
    os.remove(path)
    tea.save()
    about_banner.objects.get(id=request.GET['id']).delete()
    request.session['delete_data_session'] = 1
    return HttpResponse("OK")

@login_required(login_url="/admin-side/")
def get_about_image(request):
    tea = about_banner.objects.get(id=request.GET.get('id'))
    data = {
        'id': tea.id,
        'name': tea.text,
    }
    return JsonResponse({"data": data})

@login_required(login_url="/admin-side/")
def contact_status(request):
    con = contact.objects.get(id=request.GET.get('id'))
    if con.status:
        con.status = False
    else:
        con.status = True
    con.save()
    return JsonResponse({"data": "ok"})

@login_required(login_url="/admin-side/")
def forgot_password(request):
    return render(request, 'forgotpassword.html')

@login_required(login_url="/admin-side/")
def change_password(request):
    if request.method == "POST":
        confpassword = request.POST["confpassword"]
        password = request.POST["password"]
        if (confpassword != "" and password != "") and ( confpassword == password ):
            user = User.objects.get(id=request.session['id'])
            user.set_password(password)
            user.save()
            return redirect("/admin-side/dashboard/")
        else:
            return render(request, "forgotpassword.html",{"error":"Password must be same..."})
    return render(request,"forgotpassword.html")
