from django.views.generic import base
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from pswebsite.forms import RegisterForm

# TODO: decorate user views with login_requiered

class PsTemplateView(base.TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context

class IndexView(PsTemplateView):
    template_name = 'pswebsite/index.html'
    page_title = 'Home'

class AboutView(PsTemplateView):
    template_name = 'pswebsite/about.html'
    page_title = 'About'

class UserView(PsTemplateView):
    template_name = 'pswebsite/user.html'
    page_title = 'User'

class Register(CreateView):
    template_name = 'pswebsite/register.html'
    page_title = 'Register'
    model = User
    form_class = RegisterForm

    def get_success_url(self):
        return reverse('pswebsite:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context

    def post(self, request):
        res = super().post(request)
        
        # if the form is valid and we have registered, log the user in too
        form = self.form_class(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['email'],
                                     password=form.cleaned_data['password1'])
            auth.login(request, user)

        return res

class UserExists(base.View):
    """ Validates a parsley.js ajax call to see if an email is taken """
    def get(self, request):
        username = None
        if 'username' in request.GET:
            username = request.GET['username']
        else:
            username = request.GET['email']

        user = get_object_or_404(User, username=username)
        return HttpResponse()
