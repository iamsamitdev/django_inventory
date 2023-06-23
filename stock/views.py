from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Import Product model
from .models import Product

# Frontend views
def index(request):
    return render(request, 'frontend/index.html')


def about(request):
    return render(request, 'frontend/about.html')


def register(request):
    return render(request, 'auth/register.html')


def login_request(request):
    # รับค่าจากฟอร์ม
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        # ตรวจสอบว่ามี user นี้ในระบบหรือไม่
        if user is not None:

            # เก็บ session ของ user ที่ login สำเร็จ
            request.session['firstname'] = user.first_name
            request.session['lastname'] = user.last_name
            request.session['email'] = user.email
            
            login(request, user)
            return redirect('dashboard') # ไปยังหน้า dashboard
        else:
            messages.error(request, 'Invalid login')
            return redirect('login') # ไปยังหน้า login

    return render(request, 'auth/login.html')

# Backend views
@login_required(login_url='login')
def dashboard(request):
    
    # Check session
    if 'firstname' in request.session:
        firstname = request.session['firstname']
        lastname = request.session['lastname']
        email = request.session['email']

        params = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email
        }

    return render(request, 'backend/dashboard.html', {'params': params})


# Read Products
@login_required(login_url='login')
def products(request):

    # Check session
    if 'firstname' in request.session:
        firstname = request.session['firstname']
        lastname = request.session['lastname']
        email = request.session['email']

        params = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email
        }

    # Read Products
    products = Product.objects.all() # ดึงข้อมูลทั้งหมดจาก Product model

    # retrive data from form
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_detail = request.POST.get('product_detail')
        product_barcode = request.POST.get('product_barcode')
        product_qty = request.POST.get('product_qty')
        product_price = request.POST.get('product_price')
        product_image = request.POST.get('product_image')
        product_status = request.POST.get('product_status')

        # Create Product
        product = Product(
            product_name=product_name,
            product_detail=product_detail,
            product_barcode=product_barcode,
            product_qty=product_qty,
            product_price=product_price,
            product_image=product_image,
            product_status=product_status
        )

        product.save()
        messages.success(request, 'Product has been created successfully.')


    return render(request, 'backend/products.html',
        {
            'products': products, 
            'params': params
        }
    )


def logout_request(request):

    logout(request) # ออกจากระบบ
    # ลบ session ทั้งหมด
    request.session.flush()
    return redirect('login')