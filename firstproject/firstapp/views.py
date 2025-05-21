from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm
# Create your views here.
def hello_world(request):
    return HttpResponse("HELLO WORLD")
class helloEhtopia(View):
    def get(self,request):
        return HttpResponse("HELLO EHOPIA")
def home(request):
    form = ReservationForm()
    if request.method == 'POST':
        form= ReservationForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponse("Form submitted successfully!")
    return render(request, 'index.html', {'form': form})
