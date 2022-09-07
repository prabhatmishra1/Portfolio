from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from prabhat.forms import ContactForm
from prabhat.models import Contact
# Create your views here.

class MyView(View):
    def get(self, request):
        form=ContactForm()
        return render(request,'prabhat/index.html',{'form':form})
    
    def post(self,request):
        form=ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return JsonResponse({'messages':'done'})
        else:
            data={'messages':'Something went wrong'}
            return JsonResponse(data)
