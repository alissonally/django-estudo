from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.IndexView.home, name="home"),
    url(r'^(?P<post_slug>\S+)$', views.Single.single, name='single'),
]
