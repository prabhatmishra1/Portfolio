from django import forms

class  ContactForm(forms.Form):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control','id': 'inputText' ,'placeholder':'Your name', 'name':'name'}))
    email = forms.EmailField(label='',max_length=100,widget=forms.EmailInput(attrs={'class': 'form-control','id': 'inputEmail','placeholder':'Your email','name':'email'}))
    subject = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control','id': 'inputSubject','placeholder':'Subject', 'name':'subject'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'wpcf7-form-control wpcf7-textarea form-control','id':'inputMessage','cols':40,'rows':4,'placeholder': 'Message...', 'name': 'message'}))
