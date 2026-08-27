from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Bienvenidos</h1>"
"<p style= 'color:blue'> Todo lo que necesitas </p>")
