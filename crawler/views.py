from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_in
from django.shortcuts import render, render_to_response, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView
from signals.handlers import crawl_data_and_save_in_db

from .models import NewsItem
from .forms import UserCreationForm


class NewsItemListView(ListView):
    model = NewsItem
    context_object_name = 'news_items'
    ordering = '-id'

    def get_queryset(self):
        user_logged_in.connect(crawl_data_and_save_in_db, sender=settings.AUTH_USER_MODEL)
        return NewsItem.objects.all()


def sign_up(request):

    context = RequestContext(request)
    already_registered = False

    if request.method == 'POST':
        user_form = UserCreationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            already_registered = True
        else:
            print user_form.errors
    else:
        user_form = UserCreationForm()
    return render_to_response('crawler/sign_up.html',
                              {'user_form': user_form, 'registered': already_registered}, context)


def user_login(request):

    context = RequestContext(request)
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/news/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(email, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('crawler/login.html', {}, context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def home(request):
    context = RequestContext(request)
    return render_to_response('crawler/home.html', {}, context)