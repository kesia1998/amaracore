from django.shortcuts import render

import requests

# Create your views here.
def clist(request):
    response=requests.get('https://60ac9dff9e2d6b0017457815.mockapi.io/ag/contacts').json()
    return render(request,'contact.html',{'response':response})

