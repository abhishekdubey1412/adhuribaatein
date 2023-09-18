from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import UserProfile
from services.views import page_data

def registration(request):
    page_data['title'] = 'Sing Up'
    page_data['description'] = 'a picture in words of somebody/something or of something that happened'
    
    if not page_data['active_user']:
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
                return redirect("loginsuer")

        return render(request, 'registration.html', {'page_data':page_data})
    
    else:
        return redirect('user_dashboard')


def loginsuer(request):
    page_data['title'] = 'Sign In'
    page_data['description'] = 'a picture in words of somebody/something or of something that happened'

    if not page_data['active_user']:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            if UserProfile.objects.filter(username=username).exists() and check_password(password, UserProfile.objects.get(username=username).password):
                page_data['active_user'] = True
                url = f"/user_dashboard/?user={username}"
                return redirect(url)
            else:
                page_data['sign_in'] = True
            
        return render(request, 'registration.html', {'page_data':page_data})
    else:
        return redirect('user_dashboard')


active_username = ""
def user_dashboard(request):
    global active_username
    page_data['title'] = 'Dashboard'
    page_data['description'] = 'a picture in words of somebody/something or of something that happened'

    if request.method == "GET":
        active_user = request.GET.get('user')

        if active_user != None:
            active_username = active_user

        if request.GET.get('user') != None and not page_data['active_user'] and active_username == "":
            return redirect('registration')
        elif request.GET.get('user') != None and page_data['active_user'] and active_username != "":
            user_data = UserProfile.objects.get(username=active_username)
            return render(request, 'user_dashboard.html', {'page_data':page_data, 'user_data':user_data})
        elif page_data['active_user'] and active_username != "":
            url = f"/user_dashboard/?user={active_username}"
            return redirect(url)
        else:
            return redirect('registration')
    
    if request.method == "POST":
        edit = request.POST.get('edit')
        if edit:
            edit_data = UserProfile.objects.get(username=active_username)
            return render(request, 'edit_user.html', {'edit_data':edit_data, 'page_data':page_data})
        
def edit_user(request):
    global active_username
    if request.method == 'POST':
        # Retrieve form data from the POST request
        name = request.POST['name']
        username = request.POST['username']
        description = request.POST['description']
        user_id = request.POST['user_id']
        profile_img = request.FILES.get('profile_img')

        # Assuming you have a custom User model named UserProfile
        # Retrieve the user object to update (replace with your logic)
        user = UserProfile.objects.get(id=user_id)

        # Update the user's information
        user.name = name
        user.username = username
        user.description = description
        user.save()

        if profile_img:
            user.image = profile_img  # Assuming 'image' is a field in the UserProfile model
            user.save()

        active_username = username

        # Redirect to a different page after a successful update
        return redirect('user_dashboard')  # Replace 'user_dashboard' with your desired URL

    # Handle GET request or render the form for the first time
    return redirect('user_dashboard')