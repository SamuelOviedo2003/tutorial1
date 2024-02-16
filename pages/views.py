from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView 
from django.views import View 
from django import forms
# Create your views here.
class HomePageView(TemplateView): 
    template_name = "pages\home.html"

class AboutPageView(TemplateView): 
    template_name = 'pages/about.html'

class ContactPageView(TemplateView): 
    template_name = 'pages/contact.html'  

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "title": "About us - Online Store", 
            "subtitle": "About us", 
            "description": "This is an about page ...", 
            "author": "Developed by: Your Name", 
        }) 
        return context

class Product: 
    products = [ 
        {"id":"1", "name":"TV", "description":"Best TV", "price":101}, 
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":50}, 
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":60}, 
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":70} 
    ] 

class ProductIndexView(View): 
    template_name = 'products/index.html' 
    def get(self, request): 
        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] =  "List of products" 
        viewData["products"] = Product.products 
        return render(request, self.template_name, viewData) 

class ProductShowView(View): 
    template_name = 'products/show.html' 

    def get(self, request, id): 
        viewData = {} 
        if int(id) <= len(Product.products):
            product = Product.products[int(id)-1] 
            viewData["title"] = product["name"] + " - Online Store" 
            viewData["subtitle"] =  product["name"] + " - Product information"
            viewData["price"] =  str(product["price"]) + " - Price"  
            viewData["product"] = product 
        else:
            return HttpResponseRedirect('http://127.0.0.1:8000/')

        return render(request, self.template_name, viewData)

class ProductForm(forms.Form): 
    name = forms.CharField(required=True) 
    price = forms.DecimalField(required=True, min_value=0.0)



class ProductCreateView(View): 
    template_name = 'products/create.html' 
    def get(self, request): 
        form = ProductForm() 
        viewData = {} 
        viewData["title"] = "Create product" 
        viewData["form"] = form 
        return render(request, self.template_name, viewData) 
 
    def post(self, request): 
        form = ProductForm(request.POST) 
        if form.is_valid() and form.errorMenorZero:  
            return render(request,"pages/success.html") 
        else: 
            viewData = {} 
            viewData["title"] = "Create product" 
            viewData["form"] = form 
            return render(request, self.template_name, viewData)