from django.conf.urls import url
from blogblog import views
from django.contrib import admin

urlpatterns = [
	url(r'^$', views.LogIn, name='login'),
    url(r'^blogblog/youser$', views.Youser, name='youser'),
    url(r'^blogblog/estcost$', views.Estimate, name='estcost'),
    url(r'^blogblog/ordslip$', views.OrderSlip, name='ordslip'),
    url(r'^blogblog/mess$', views.Design, name='mess'),
    url(r'^blogblog/inq$', views.Inquiry, name='inq'),
    url(r'^blogblog/profile$', views.Profile, name='profile'),
    # url(r'^blogblog/que/$', views.addquery, name='que'),
    # url(r'^blogblog/message/$', views.message, name='message'),
	# url(r'^blogblog/(\d+)/$', views.OrderDetails, name='orderdetails'),
	# url(r'^blogblog/newlist_url$', views.NewOrder, name='neworder'),
	# url(r'^blogblog/(\d+)/addItem$', views.AddOrder, name='addorder'),
	url('admin/', admin.site.urls),
	]



"""Blogta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]"""
