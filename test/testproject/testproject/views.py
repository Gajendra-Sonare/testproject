from django.http import HttpResponse

# print hello world in django
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
