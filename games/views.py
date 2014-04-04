from django.shortcuts import render, redirect
from games.models import Game, Wishlist
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse_lazy
from django.template import add_to_builtins
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse

def index(request):
        games_list = Game.objects.filter(onsale=1)[:16]
        template = loader.get_template('games/index.html')
        context = RequestContext(request, {
                'games_list': games_list,
        })
        return HttpResponse(template.render(context))

def all_games(request):
        allgames = Game.objects.all().order_by('-drp')
        paginator = Paginator(allgames, 20)
        page = request.GET.get('page')
        try:
                games = paginator.page(page)
        except PageNotAnInteger:
                games = paginator.page(1)
        except EmptyPage:
                games = paginator.page(paginator.num_pages)
        
        return render_to_response('games/all.html', {"games": games })
        
def deals(request):
        deals_list = Game.objects.filter(onsale=1)
        template = loader.get_template('games/deals.html')
        context = RequestContext(request, {
                'deals_list': deals_list,
        })
        return HttpResponse(template.render(context))
        
def contact(request):
    t = TemplateResponse(request, 'games/contact.html', {})
    return HttpResponse(t.render())
    

def login(request):
    next = '/games/'
    return HttpResponseRedirect(request.POST.get('next'))

