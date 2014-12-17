from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'figexample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^components/', include('component.urls')),
    url(r'^router/', include('router.urls')),
    url(r'^runtime/', include('runtime.urls')),
)
