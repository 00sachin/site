from django.shortcuts import render
from.models import Person
from.forms import MyForm


# Create your views here.
def index(request):
    return render(request,'index.html')   
def resume(request):
    return render(request,'resume.html')
def portfolio(request):
    return render(request,'portfolio.html') 
def contacts(request):
    return render(request, 'contacts.html')  
def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'cv-form.html', {'form': form})



  
