"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from mysite.views import hello, current_datetime, hours_ahead, display_meta	#首先import
from books import views as views_b
from contact import views as views_c

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),     # 找到网址里有/hello/就去call views.py 里的 hello
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),     #re
    url(r'^meta/$', display_meta),
    url(r'^search_form/$', views_b.search_form),
    url(r'^search/$', views_b.search),
    url(r'^contact/$', views_c.contact),
    url(r'^contact/thanks/$', views_c.thanks),
]
