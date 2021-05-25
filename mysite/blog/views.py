from django.http import HttpResponse
import json
# Create your views here.

def index(data):
        data = {"Name" : "Dharati Shah",
        "Track" : "Backend (Python)",
        "Message" : "Hi, Mentor, Thank you for teaching us coding in Python !"}
        return HttpResponse(json.dumps(data))