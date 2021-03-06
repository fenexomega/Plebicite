from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    
    url(r'^$','Pleby.views.index',name="index"),
    url(r'^login$','Pleby.views.login_user',name="login"),
    url(r'^registrar$','Pleby.views.registrar',name="registrar"),
    url(r'^enquete/(?P<id>\d+)$','Pleby.views.detail_enquete',name="detail_enquete"),
    url(r'^log_out$','Pleby.views.log_out',name="log_out"),
    url(r'^create_enquete$','Pleby.views.create_enquete',name="create_enquete"),
    url(r'^tag/(?P<titulo>.+)$','Pleby.views.list_enquetes_by_tag',name="list_enquetes_by_tag")
)
