from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
page_data = {}

def home(request):
    page_data['title'] = 'Adhuri Bateein'
    page_data['description'] = 'a picture in words of somebody/something or of something that happened'
    return render(request, 'home.html', page_data)

def about(request):
    page_data['title'] = 'About Us'
    page_data['description'] = 'a picture in words of somebody/something or of something that happened'
    return render(request, 'about-us.html', page_data)

def registration(request):
    page_data['title'] = 'LogIn'
    page_data['description'] = 'a picture in words of somebody/something or of something that happened'
    return render(request, 'registration.html', page_data)

def love(request):
    page_data['title'] = 'Love'
    page_data['description'] = 'a picture in words of somebody/something or of something that happened'
    return render(request, 'home.html', page_data)

def sad(request):
    page_data['title'] = 'Sad'
    page_data['description'] = 'a picture in words of somebody/something or of something that happened'
    return render(request, 'home.html', page_data)

def romantic(request):
    page_data['title'] = 'Romantic'
    page_data['description'] = 'a picture in words of somebody/something or of something that happened'
    return render(request, 'home.html', page_data)

def story(request):
    page_data['title'] = 'Story'
    page_data['description'] = 'a picture in words of somebody/something or of something that happened'
    return render(request, 'home.html', page_data)

def get_user_ip(request):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        # The header may contain multiple IP addresses, so split them and get the first one
        user_ip = user_ip.split(',')[0].strip()
    else:
        # If the header is not present, fall back to 'REMOTE_ADDR'
        user_ip = request.META.get('REMOTE_ADDR')

    return HttpResponse(f'Your IP address is: {user_ip}')