from django.http import HttpResponse
import json 

def index(request):
    
    dict1={
        "name":"John",
        "age":30,
        "city":"New York"
    }

    return HttpResponse(json.dumps(dict1), content_type="application/json")


