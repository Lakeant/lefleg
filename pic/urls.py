from django.conf.urls import url
from . import views 
urlpatterns=[

	url(r'^$',views.index,name='index'),
        url(r'^blog/$',views.blog,name='blog'),
        url(r'contact$',views.contact,name='contact'),
        url(r'gallery\_horizontal\_static$',views.gallery_horizontal_static,name='gallery_horizontal_static'),
        url(r'index$',views.index,name='index'),
        url(r'single$',views.single,name='single'),
        url(r'single\_portfolio\_image$',views.single_portfolio_image,name='single_portfolio_image'),
        url(r'team\_horizontal$',views.team_horizontal,name='team_horizontal'),
        url(r'blog\_large$',views.blog_large,name='blog_large'),
        url(r'features$',views.features,name='features'),
        url(r'gallery$',views.gallery,name='gallery'),
        url(r'sendemail\_phpsingle\_portfolio\_gallery$',views.sendemail_phpsingle_portfolio_gallery,name='sendemail_phpsingle_portfolio_gallery'),
        url(r'single\_team2$',views.single_team2,name='single_team2'),
        url(r'team$',views.team,name='team'),
        url(r'blog\_medium$',views.blog_medium,name='blog_medium'),
        url(r'gallery\_horizontal$',views.gallery_horizontal,name='gallery_horizontal'),
        url(r'gallery\_static$',views.gallery_static,name='gallery_static'),
        url(r'single2$',views.single2,name='single2'),
        url(r'single\_portfolio$',views.single_portfolio,name='single_portfolio'),
        url(r'single\_team$',views.single_team,name='single_team'),
        url(r'team\_masonry$',views.team_masonry,name='team_masonry'),

]
