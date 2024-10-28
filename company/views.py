from django.http import HttpResponse,JsonResponse

def homepage(request):
    print("home page requested")
    # return HttpResponse("Hello Welcome to Homepage")
    
    friends=[
        "ashish",
        "sachin",
        "saurav",
        "rahul",
        
        
        
        
    ]
    return JsonResponse(friends,safe=False)