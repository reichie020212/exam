from django.conf.urls import url

from . import views
from django.contrib.auth import views as loginviews

urlpatterns = [
	url(r'^$', loginviews.login,name="login"),
	url(r'^logout/$', loginviews.logout, name="logout", kwargs={'next_page': '/'}),
	url(r'^home/add/$',views.add,name="add"),
	url(r'^accounts/profile/$', views.redirecting,name="redirecting"),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^home/$',views.view_home,name="view_home"),
	url(r'^home/(?P<pk>\d+)/edit/$',views.edit,name="edit"),
	url(r'^home/(?P<pk>\d+)/$',views.displaycontact,name="displaycontact"),
	url(r'^home/(?P<pk>\d+)/delete/', views.delete, name="delete"),

]