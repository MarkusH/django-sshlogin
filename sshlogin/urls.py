from django.conf.urls import patterns, include, url
from django.contrib import admin

from keymgmt.views import sshlogin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sshlogin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sshlogin/(?P<key_string>[a-zA-Z0-9]{254})$', sshlogin, name='sshlogin'),
)
