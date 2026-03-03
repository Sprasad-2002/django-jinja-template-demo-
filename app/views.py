from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'Shiva Shanakara Rath','age':25}
    return render(request,'jinja_print.html',d)