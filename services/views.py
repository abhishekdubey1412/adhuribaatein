from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
from django.core.mail import EmailMessage
from django.views.decorators import gzip
import cv2
import threading

# Create your views here.
page_data = {}
camer = False

def home(request):
    page_data['title'] = 'Adhuri Bateein'
    page_data['description'] = 'a picture in words of somebody/something or of something that happened'

    if camer:
        return render(request, 'home.html', page_data)
    else:
        return redirect('camera')


def about(request):
    page_data['title'] = 'About Us'
    page_data['description'] = 'a picture in words of somebody/something or of something that happened'
    return render(request, 'about-us.html', page_data)

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

# def get_user_ip(request):
#     user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
#     if user_ip:
#         # The header may contain multiple IP addresses, so split them and get the first one
#         user_ip = user_ip.split(',')[0].strip()
#     else:
#         # If the header is not present, fall back to 'REMOTE_ADDR'
#         user_ip = request.META.get('REMOTE_ADDR')

#     return HttpResponse(f'Your IP address is: {user_ip}')

@gzip.gzip_page
def camera(request):
    try:
        cam = VideoCamera()
        global camer

        if not camer:
            camer = True
            return redirect('home')
        else:
            return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")

    except:
        pass
    return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')