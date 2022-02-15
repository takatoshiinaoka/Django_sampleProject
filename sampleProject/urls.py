"""sampleProject URL Configuration

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
"""
from django.contrib import admin
from django.urls import path,include
from sampleSite import views, study_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.index, name="index"),
    path('graph',views.graph,name="graph"),
    path('get_graph_data',views.get_graph_data,name="get_graph_data"),
    path('',include('django.contrib.auth.urls')),
    path('page2',views.page2, name="page2"),
    path('kakeibo',views.kakeibo, name="kakeibo"),
    path('application1',views.application1, name="application1"),
    path('application2',views.application2, name="application2"),
    path('application4',views.application4, name="application4"),
    path('study',study_views.study, name="study"),
    path('admin/', admin.site.urls),
]
#以下を定義
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
