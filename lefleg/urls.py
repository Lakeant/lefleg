"""lefleg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. 'dd a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from pic import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	
	# url(r'^$', include('pic.urls')),
	 url(r'^admin/', admin.site.urls),
        url(r'^$',views.index,name='index'),
        url(r'^index/$',views.index,name='index'),
        url(r'^blog/$',views.blog,name='blog'),
        url(r'^contact/$',views.contact,name='contact'),
        url(r'^gallery-horizontal-static/$',views.gallery_horizontal_static,name='gallery_horizontal_static'),
        url(r'^index/$',views.index,name='index'),
        url(r'^single/$',views.single,name='single'),
        url(r'^single-portfolio-image/$',views.single_portfolio_image,name='single_portfolio_image'),
        url(r'^team-horizontal/$',views.team_horizontal,name='team_horizontal'),
        url(r'^blog-large/$',views.blog_large,name='blog_large'),
        url(r'^features/$',views.features,name='features'),
        url(r'^gallery/$',views.gallery,name='gallery'),
        url(r'^sendemail-phpsingle-portfolio-gallery/$',views.sendemail_phpsingle_portfolio_gallery,name='sendemail_phpsingle_portfolio_gallery'),
        url(r'^single-team2/$',views.single_team2,name='single_team2'),
        url(r'^team/$',views.team,name='team'),
        url(r'^blog-medium/$',views.blog_medium,name='blog_medium'),
        url(r'^gallery-horizontal/$',views.gallery_horizontal,name='gallery_horizontal'),
        url(r'^gallery-horizontal-static/$',views.gallery_horizontal_static,name='gallery_horizontal_static'),
        url(r'^gallery-static/$',views.gallery_static,name='gallery_static'),
        url(r'^single2/$',views.single2,name='single2'),
        url(r'^single-portfolio/$',views.single_portfolio,name='single_portfolio'),
        url(r'^single-portfolio-gallery/$',views.single_portfolio_gallery,name='single_portfolio_gallery'),
        url(r'^single-team/$',views.single_team,name='single_team'),
        url(r'^team-masonry/$',views.team_masonry,name='team_masonry'),

]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)