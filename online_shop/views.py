from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import Product, Profile, Contact


# Create your views here.

def home(request):
    message = "Hello Everyone Welcome to my Blogging Page"
    context = {"message": message}
    # set value on session
   # request.session["online_shop"] = "Welcome to my Blogging Page"
    return render(request, "home.html")


def product(request, product_id):
    return render(request, 'product_detail.html')
def product_list(request):
    # Query the database to get a list of all products
    products = Product.objects.all()

    return render(request, 'product_list.html', {'products': products})
def product_detail(request):
    return render(request, 'product_detail.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def register(request):
    # Adding logic view to render registration page
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match. Please try again.")
        else:
            # Check if the email is already in use
            if User.objects.filter(username=email).exists():
                messages.error(request, "Email is already in use. Please use a different email.")
            else:
                # Create a new user

                user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
                messages.success(request, "Registration successful. You can now log in.")
                return redirect('login')  # Redirect to the login page
    return render(request, 'register.html')

def log_in(request):
    # Add your logic here to render the login page
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            # User is authenticated and logged in, you can redirect to a success page or do something else here.
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')
    return render(request, 'login.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if name:
            contact.name = name

        if email:
            contact.email = email

        if subject:
            contact.subject = subject

        if message:
            contact.message = message


        # Save the contact data to the database
        contact_data = {"name": name, "email": email, "message": message}
        print(contact_data)
        Contact.objects.create(**contact_data)
        messages.info(request, message="We have received your message and will get back to you shortly")
        return redirect("contact")
    return render(request, 'contact.html')

@login_required
def profile_page(request):
    # get value on session
    # print("request.session:", request.session.get("blog"))
    profile = {}
    if Profile.objects.filter(user__email=request.user.email).exists():
        profile = Profile.objects.get(user__email=request.user.email)
        if request.method == "POST":
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            mobile = request.POST.get("mobile")
            email = request.POST.get("email")
            address = request.POST.get("address")
            if first_name:
                profile.first_name = first_name
            if last_name:
                profile.last_name = last_name
            if mobile:
                profile.mobile = mobile
            if email:
                profile.email = email
            if address:
                profile.address = address
            profile.save()
            messages.info(request, message="Profile updated Successfully")
            return redirect("profile_page")
    context = {"profile": profile}
    return render(request, "profile.html", context)