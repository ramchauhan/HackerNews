from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from .models import NewsItem
from .forms import UserCreationForm


class NewsItemListView(ListView):
    """
    News List View to display the all news on dashboard
    """
    model = NewsItem
    context_object_name = 'news_items'

    def get_queryset(self):
        return NewsItem.objects.exclude(deleted_item=True)


def sign_up(request):
    """
    View for sign up with the application
    :param request:
    :return: response
    """
    context = RequestContext(request)
    already_registered = False

    if request.method == 'POST':
        user_form = UserCreationForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            already_registered = True
        else:
            print user_form.errors
    else:
        user_form = UserCreationForm()
    return render_to_response('crawler/sign_up.html',
                              {'user_form': user_form, 'registered': already_registered}, context)


def user_login(request):
    """
    Login view to login in the application
    :param request:
    :return: response object
    """
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
    """
    View to be used for logout the user from application
    :param request:
    :return:
    """
    logout(request)
    return HttpResponseRedirect('/')


def home(request):
    """
    Home view
    """
    context = RequestContext(request)
    return render_to_response('crawler/home.html', {}, context)


@csrf_exempt
def delete_news(request, pk):
    """
    this view is used to update the deleted_item column for a news from the dashboard softly not permanently
    :param request:
    :param pk:
    :return: JsonResponse object
    """
    if request.is_ajax():
        deleted_news = NewsItem.objects.get(id=pk)
        deleted_news.deleted_item = True
        deleted_news.save()
        return JsonResponse({
            'status': 'successfully deleted'
        })


@csrf_exempt
def read_news(request, pk):
    """
    this view is used for update the read_item column if user is already went through the news
    :param request:
    :param pk:
    :return:
    """
    if request.is_ajax():
        news_you_read = NewsItem.objects.get(id=pk)
        if not news_you_read.read_item:
            news_you_read.read_item = True
            news_you_read.save()
        return JsonResponse({
            'status': 'successfully updated your record'
        })