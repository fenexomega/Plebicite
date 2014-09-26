from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    
    url(r'^$','Pleby.views.index',name="index"),
    url(r'^login$','Pleby.views.login_user',name="login"),
    url(r'^create_usuario$','Pleby.views.create_usuario',name="create_usuario"),
    url(r'^enquete_detail_(?P<id>\d+)$','Pleby.views.detalhe_enquete',name="detalhe_enquete"),
    url(r'^log_out$','Pleby.views.log_out',name="log_out"),
    url(r'^create_enquete$','Pleby.views.create_enquete',name="create_enquete")
)
