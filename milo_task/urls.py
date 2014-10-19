from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'milo_task.account.views.listing'),
    url(r'^view/(?P<user_id>\d+)$', 'milo_task.account.views.display'),
    url(r'^edit/(?P<user_id>\d+)$', 'milo_task.account.views.edit'),
    url(r'^create', 'milo_task.account.views.create'),
    url(r'^delete/(?P<user_id>\d+)$', 'milo_task.account.views.delete'),
    url(r'^export_csv', 'milo_task.account.views.export_csv'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
