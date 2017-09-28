from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from common_db  import *
# Create your views here.

def index(request):

    pic_list=custom_sql("select id,img_url from pic_image_main")

    return render_to_response('index.html',{'test':"Hello, world. You're at the polls index."})
	#return HttpResponse("Hello, world. You're at the polls index.")
                                                                                                                                                                                    

def blog(request):
                return render_to_response('blog.html',{'test':"Hello, world. You're at the polls index."})

def contact(request):
                return render_to_response('contact.html',{'test':"Hello, world. You're at the polls index."})

def gallery_horizontal_static(request):
                return render_to_response('gallery-horizontal-static.html',{'test':"Hello, world. You're at the polls index."})


def single(request):
                return render_to_response('single.html',{'test':"Hello, world. You're at the polls index."})

def single_portfolio_image(request):
                return render_to_response('single-portfolio-image.html',{'test':"Hello, world. You're at the polls index."})

def team_horizontal(request):
                return render_to_response('team-horizontal.html',{'test':"Hello, world. You're at the polls index."})

def blog_large(request):
                return render_to_response('blog-large.html',{'test':"Hello, world. You're at the polls index."})

def features(request):
                return render_to_response('features.html',{'test':"Hello, world. You're at the polls index."})

def gallery(request):
                return render_to_response('gallery.html',{'test':"Hello, world. You're at the polls index."})

def sendemail_phpsingle_portfolio_gallery(request):
                return render_to_response('sendemail.phpsingle-portfolio-gallery.html',{'test':"Hello, world. You're at the polls index."})

def single_team2(request):
                return render_to_response('single-team2.html',{'test':"Hello, world. You're at the polls index."})

def team(request):
                return render_to_response('team.html',{'test':"Hello, world. You're at the polls index."})

def blog_medium(request):
                return render_to_response('blog-medium.html',{'test':"Hello, world. You're at the polls index."})

def gallery_horizontal(request):
                return render_to_response('gallery-horizontal.html',{'test':"Hello, world. You're at the polls index."})

def gallery_static(request):
                return render_to_response('gallery-static.html',{'test':"Hello, world. You're at the polls index."})

def single2(request):
                return render_to_response('single2.html',{'test':"Hello, world. You're at the polls index."})

def single_portfolio(request):
               return render_to_response('single-portfolio.html',{'test':"Hello, world. You're at the polls index."})

def single_portfolio_gallery(request):
               return render_to_response('single-portfolio-gallery.html',{'test':"Hello, world. You're at the polls index."})
def single_team(request):
                return render_to_response('single-team.html',{'test':"Hello, world. You're at the polls index."})

def team_masonry(request):
               return render_to_response('team-masonry.html',{'test':"Hello, world. You're at the polls index."})
                                                    
