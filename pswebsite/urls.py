from django.conf.urls import url

from django.views.generic.edit import CreateView

from django.contrib.auth import views as auth_views
from django.contrib.auth import forms

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^user/$', views.UserView.as_view(), name='user'),
    url(r'^login/$',
        auth_views.login,
        {
            'template_name': 'pswebsite/login.html',
            'extra_context': {'page_title': 'Login'},
        },
        name='login'
    ),
    url(r'^logout/$',
        auth_views.logout,
        {
            'next_page': 'pswebsite:index',
        },
        name='logout'
    ),
    url(r'^register/$', views.Register.as_view(), name='register'),

    # ajax method
    url(r'^validate/userexists/$', views.UserExists.as_view(), name='userexists'),

    # the next two are both for detail views of posters
    url(r'^poster/(?P<pk>[0-9]+)/$',
        views.PosterDetailWithoutSlugRedirectView.as_view(),
        name='poster-without-slug'),

    url(r'^poster/(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/$',
        views.PosterDetailView.as_view(), name='poster'),
]
