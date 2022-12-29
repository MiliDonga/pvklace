from json import dumps

from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from pvkadmin.models import category, home_banner, team, product, inquiry, about_banner, contact, product_photo


def index(request):
    cat = category.objects.all().filter(is_active=True).values()
    home = home_banner.objects.all().values()
    data = {
        'category': cat,
        'banner': home,
    }
    return render(request,"index.html",data)

def about(request):
    tea = team.objects.all().filter(is_active=True).values()
    abo = about_banner.objects.all().values()
    data = {
        'team': tea,
        'banner': abo[0]['banner_image'],
        'slide':abo[1:]
    }
    return render(request,"about.html",data)

def contact_page(request):
    return render(request,"contact.html")

def artwork(request):
    cat = category.objects.all().filter(is_active=True).values()
    pro = product.objects.all().filter(is_active=True).values()
    for item in pro:
        id = item['category']
        item['category'] = category.objects.get(id=id).category_name
    data = {
        'category': cat,
        'product': pro,
        'dat':''
    }
    return render(request,"artwork.html",data)

def artwork_filter(request,filter):
    cat = category.objects.all().filter(is_active=True).values()
    pro = product.objects.all().filter(is_active=True).values()
    for item in pro:
        id = item['category']
        item['category'] = category.objects.get(id=id).category_name
    data = {
        'category': cat,
        'product': pro,
        'dat':filter
    }
    return render(request,"artwork.html",data)

def add_inquiry(request):
    if request.method == 'POST':
        pro = product.objects.get(id=request.POST['item_name'])
        cat = category.objects.get(id=pro.category)
        inq = inquiry(name=request.POST['name'],email=request.POST['email'],contact_no=request.POST['contact'],item_name=pro.product_name,category=cat.category_name)
        inq.save()
        request.session['add'] = 1
        return redirect("/artwork/")

def add_session(request):
    request.session['add'] = 0
    return HttpResponse('ok')

def get_in_touch(request):
    if request.method == 'POST':
        inq = contact(name=request.POST['name'],email=request.POST['email'],contact_no=request.POST['phone'],subject=request.POST['subject'],message=request.POST['message'])
        inq.save()
        request.session['add'] = 1
        return redirect("/artwork/")

def get_product_image(request):
    pro = product_photo.objects.all().filter(product_id=request.GET.get('id')).values()
    image = []
    if len(pro) > 0:
        for data in pro:
            print(data['image'])
            image.append(str(data['image']))
    else:
        pro = product.objects.get(id=request.GET.get('id'))
        image.append(str(pro.product_image))
    return JsonResponse({"data": image})
