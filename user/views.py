from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import UserProfile

def registration(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if the username or email already exists in the database
        if UserProfile.objects.filter(username=username).exists() or UserProfile.objects.filter(email=email).exists():
            # You can handle this case with an error message or redirect back to the registration page
            return render(request, 'registration.html', {'error_message': 'Username or email already exists.'})

        # Validate and sanitize input data
        else:
            # Hash the password
            hashed_password = make_password(password)

            # Create a new user profile
            user_profile = UserProfile(name=name, username=username, email=email, password=hashed_password)
            user_profile.save()

            # Redirect to the home page after successful registration
            return redirect("home")

    return render(request, 'registration.html')

def loginsuer(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if check_password(password, UserProfile.objects.get(username=username).password):
            return redirect("home")
        
    return render(request, 'registration.html')