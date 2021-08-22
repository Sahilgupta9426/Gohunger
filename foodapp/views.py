from django.shortcuts import render,HttpResponse
from .forms import ContactReg ,CustomerProfileForm
from .models import Contact,Menu,Cart,OrderPlaced,Customer
from django.contrib import messages
# from django.core.paginator import Paginator
from django.views import View

from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class ProductView(View):
	def get(self, request):
		
		veg = Menu.objects.filter(category='N')
		nonveg = Menu.objects.filter(category='V')
		sweet = Menu.objects.filter(category='SE')

		
		return render(request, 'htmls/meals.html', {'veg':veg,'nonveg':nonveg,'sweets':sweet})


def index(request):
    return render(request, 'htmls/index.html')

def about(request):
    return render(request, 'htmls/about.html')

# def meals(request):
#     # meal_obj=Menu.objects.all()
#     all_post=Menu.objects.all().order_by('id')
#     # pagignator=Paginator(all_post,3,orphans=1)
#     pagignator=Paginator(all_post,6)
#     page_number=request.GET.get('page')
#     meal_obj=pagignator.get_page(page_number)    
#     return render(request, 'htmls/meals.html',{'meal':meal_obj} )

def signup(request):
    pass

def login(requset):
    return render(requset,'htmls/login.html')

def ContactUS(request):
    if request.method=='POST':
        fm=ContactReg(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            num=fm.cleaned_data['number']
            det=fm.cleaned_data['details']
            
            reg=Contact(name=nm,email=em,number=num,details=det)
            # fm.save()
            reg.save()
            fm=ContactReg()
            messages.success(request, 'Form submission successful')
    else:
        fm=ContactReg()
    cont=Contact.objects.all()

    
    return render(request,'htmls/contact.html',{'form':fm,'conts':cont})



