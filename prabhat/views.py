from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.views import View
from django.core.mail import send_mail
from . forms import ContactForm
# Create your views here.

class MyView(View):
    def get(self, request):
        # <view logic>
        form=ContactForm()
        return render(request,'prabhat/index.html',{'form':form})

    def post(self,request):
        form=ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipients = ['mishraa.prabhat@gmail.com']
            print(name)
            if sender:
                #send_mail(subject, "Name: "+name+"\nEmail: "+sender+"\n\n"+message, sender, recipients)
                data={'messages':'done'}
                return JsonResponse(data)
            else:
                data={'messages':'Data has not been saved successfully'}
                return JsonResponse(data)
