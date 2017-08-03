from django.conf.urls import url
from plannerpages import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
    url(r'^year/$', views.YearPageView.as_view()), # Add this /year/ route
    url(r'^year/$', views.YearPageView.as_view()),
]
