from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth import  logout
from django.contrib import  messages
from django.urls import  reverse
from django.views.generic import  CreateView,FormView,DetailView,View,UpdateView
from django.views.generic.edit import FormMixin
from django.shortcuts import  render,redirect
from django.utils.safestring import mark_safe

from property.mixins import  NextUrlMixin,RequestFormAttachMixin
from .forms import  LoginForm,RegisterForm, ReactivateEmailForm,UserDetailChangeForm
from .models import EmailActivation


class AccountEmailActivateView(FormMixin,View):
    success_url = '/accs/login/'
    form_class = ReactivateEmailForm
    key = None

    def get(self,request,key=None, *args, **kwargs):
        self.key = key
        if key is not None:
            qs = EmailActivation.objects.filter(key__iexact=key)
            confirm_qs = qs.confirmable()
            if confirm_qs.count() == 1:
                obj = confirm_qs.first()
                obj.activate()
                messages.success(request,'Your email has been confirmed. Please login')
                return redirect('accs:login')


            else:
                activated_qs = qs.filter(activated= True)
                if activated_qs.exists():
                    reset_link = reverse("password-reset")
                    msg = """Your email has already been confirmed
                                        Do you need to <a href="{link}">reset your password</a>?
                                        """.format(link=reset_link)
                    messages.success(request, mark_safe(msg))
                    return redirect("login")
        context = {
            'form':self.get_form(),
            'key':key
        }
        return render(request,'registration/activation-error.html',context)


    def post(self,request,*args,**kwargs):
        #Create a form to receive an email
        form = self.get_form()

        if form.is_valid():
            return  self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        msg = """Activation link sent,please check your email"""
        request = self.request
        messages.success(request,msg)
        email = form.cleaned_data.get("email")
        obj = EmailActivation.objects.email_exists(email).first()
        user = obj.user
        new_activation = EmailActivation.objects.create(
            user = user,
            email = email
        )
        new_activation.send_activation()
        return super(AccountEmailActivateView,self).form_valid(form)

    #incase the form was invalid
    def form_invalid(self,form):
        context = {
            'form':form,
            'key':self.key
                   }
        return  render(self.request,'registration/activation-error.html')


class LoginView(NextUrlMixin,RequestFormAttachMixin,FormView):
    form_class = LoginForm
    success_url = '/'
    template_name =  'accs/signin.html'

    default_next = '/' #Incase anything other than succesful login

    #If the Login was success full then redirect
    def form_valid(self, form):
        next_path = self.get_next_url()
        return redirect(next_path)


class RegisterView(CreateView):
    form_class =  RegisterForm
    template_name =  'accs/register.html'
    success_url = '/accs/login/'


class UserDetailUpdateView(LoginRequiredMixin,UpdateView):
    form_class =  UserDetailChangeForm
    template_name =  'accs/detail-update-view.html'


    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self,*args, **kwargs):
        context = super(UserDetailChangeForm,self).get_context_data
        context['title'] = "Update your Account"
        return context

    def get_success_url(self):
        return reverse('main:index')


def logout_view(request):
    logout(request)
    return redirect(reverse('main:index'))