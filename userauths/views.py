from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth import logout

from userauths import models as userauths_models
from userauths import forms as userauths_forms
from vendor import models as vendor_models


# Create your views here.
def register_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"You are already logged in")
        return redirect('/')   

    form = userauths_forms.UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()

        full_name = form.cleaned_data.get('full_name')
        email = form.cleaned_data.get('email')
        mobile = form.cleaned_data.get('mobile')
        password = form.cleaned_data.get('password1')
        user_type = form.cleaned_data.get("user_type")

        user = authenticate(email=email, password=password)
        login(request, user)

        messages.success(request, f"Account was created successfully.")
        profile = userauths_models.Profile.objects.create(full_name = full_name, mobile = mobile, user=user)
        if user_type == "Vendor":
            vendor_models.Vendor.objects.create(user=user, store_name=full_name)
            profile.user_Type = "Vendor"
        else:
            profile.user_Type = "Customer"
        
        profile.save()

        next_url = request.GET.get("next", 'store:index')
        return redirect(next_url)
    
    context = {
        'form':form
    }
    return render(request, 'userauths/sign-up.html', context)

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect('/')
    
    if request.method == 'POST':
        print("POST request received")  # Debug
        form = userauths_forms.LoginForm(request.POST or None)  

        if form.is_valid():
            print("Form is valid")  # Debug
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            captcha_verified = form.cleaned_data.get('captcha', False)  
            
            print(f"Email: {email}")  # Debug
            print(f"Captcha verified: {captcha_verified}")  # Debug

            if captcha_verified:
                try:
                    # Simplified and fixed authentication logic
                    user = authenticate(request, email=email, password=password)
                    print(f"Authenticated user: {user}")  # Debug
                    
                    if user is not None and user.is_active:
                        print("User is not None and active")  # Debug
                        login(request, user)
                        print("Login successful")  # Debug
                        messages.success(request, "You are Logged In")
                        next_url = request.GET.get("next", 'store:index')
                        print(f"Redirecting to: {next_url}")  # Debug
                        return redirect(next_url)
                    else:
                        print("Authentication failed or user inactive")  # Debug
                        messages.error(request, 'Invalid email or password')
                        
                except Exception as e:
                    print(f"Exception during authentication: {e}")  # Debug
                    messages.error(request, 'An error occurred during login. Please try again.')
            else:
                print("Captcha verification failed")  # Debug
                messages.error(request, 'Captcha verification failed. Please try again.')
        else:
            print("Form is not valid")  # Debug
            print(f"Form errors: {form.errors}")  # Debug

    else:
        form = userauths_forms.LoginForm()  

    context = {
        'form':form
    }
    return render(request, "userauths/sign-in.html", context)

def logout_view(request):
    if "cart_id" in request.session:
        cart_id = request.session['cart_id']
    else:
        cart_id = None
    logout(request)

    request.session['cart_id'] = cart_id
    messages.success(request, 'You have been logged out.')
    return redirect("userauths:sign-in")

# def handler404(request, exception, *args, **kwargs):
#     context = {}
#     response = render(request, 'userauths/404.html', context)
#     response.status_code = 404
#     return response

# def handler500(request, *args, **kwargs):
#     context = {}
#     response = render(request, 'userauths/500.html', context)
#     response.status_code = 500
#     return response