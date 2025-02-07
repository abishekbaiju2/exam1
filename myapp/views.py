from django.shortcuts import render
from django.views.generic import View
from myapp.forms import Product_form,Review_form
from myapp.models import Product,Review


class Product_create(View):
    
    def get(self,request):
        form=Product_form
        return render(request,'create.html',{'form': form})
    
    def post(self,request):
        form=Product_form(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
        return render(request,'create.html',{'form': form})
    
class Add_Review(View):
    def get(self,request):
        form=Review_form
        return render(request,'review.html',{'form':form})
    def post(self,request):
        form=Review_form(request.POST)
        if form.is_valid():
            Review.objects.create(**form.cleaned_data)
        return render(request,'review.html',{'form':form})
    
class View_Review(View):
    def get(self,request):
        data=Review.objects.all()
        return render(request,'view_review.html',{'data':data})


class Delete_Review(View):
    def get(self,request,**kwargs):
        id=kwargs.get('pk')
        Review.objects.get(id=id).delete()
        return render(request,'delete_review.html')


