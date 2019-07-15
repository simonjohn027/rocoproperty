from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormMixin
from .forms import ContactForm
from django.contrib import  messages
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request,'main/index.html')

def propertyList(request):
    return  render(request, 'main/properties.html')

def property(request):
    return  render(request, 'main/property.html')

def owners(request):
    return  render(request, 'main/landowner.html')

def contact(request):
    return  render(request, 'main/contact.html')

def error_404_view(request, exception):
    return render(request,'404.html')


class Contact(FormMixin,View):
    success_url = '/contact'
    form_class = ContactForm


    def get(self,request, *args, **kwargs):
        context = {
            'form':self.get_form(),
        }
        return render(request,'main/contact.html',context)


    def post(self,request,*args,**kwargs):
        #Create a form to receive an message
        form = self.get_form()

        if form.is_valid():
            return  self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        msg = """Thanks for Contact Us We will be intouch with you ASAP"""
        request = self.request
        messages.success(request,msg)
        subject = form.cleaned_data.get("subject")
        name = form.cleaned_data.get("name")
        from_email = form.cleaned_data.get("email")
        message = form.cleaned_data.get('message')
        if name and message and from_email:
            try:
                send_mail(subject=subject,message = message,from_email= from_email,recipient_list= ['simonjohn027@gmail.com',])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return super(Contact,self).form_valid(form)
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')



    #incase the form was invalid
    def form_invalid(self,form):
        msg = """Make sure all fields are entered and valid"""
        request = self.request
        messages.success(request, msg)
        context = {
            'form':form,
                   }
        return  render(self.request,'main/contact.html')




