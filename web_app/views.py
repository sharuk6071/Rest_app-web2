from django.shortcuts import render,get_object_or_404
from .models import expenses

# Create your views here.zer
expense=[
{
'name':'sai',
'income':'20000',
'expense':'13000',
'savings':'7000',
}
]


def home(request):
    context = {
        'expense':expense
    }
    return render(request,'web_app/home.html',context)
