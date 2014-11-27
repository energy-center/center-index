from django.conf.urls import patterns, include, url
import settings
#from main.views import test
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'oursite.views.home', name='home'),
    # url(r'^oursite/', include('oursite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$','main.views.index'),  
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$','main.views.index'),  
    url(r'^about/$','main.views.about'),
    url(r'^download/$','main.views.download'),
    url(r'^blog/$','main.views.blog'),
    url(r'^blog/(?P<blog_id>\d+)/$','main.views.detail',name='detail'),
    url(r'^contact/$','main.views.contact'),
    url('^user/$','main.views.user'),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',
	 {'document_root':'C:/oursite/static/', 'show_indexes': True}),
    url(r'^upload_files/(?P<path>.*)$','django.views.static.serve',
     {'document_root':'C:/upload_files/', 'show_indexes': True}),

    url(r'^test/$','main.views.test',name='test'),
    url(r'^upload/$','main.views.process_upload_file'),
    url(r'^login/$','main.views.login'),
    url(r'^logout/$','main.views.logout'),
    url(r'register/$','main.views.register'),
)

urlpatterns += patterns('',
    (r'^photologue/', include('photologue.urls')),
)