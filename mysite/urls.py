"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from hello.views import myview
from todo.views import todoView
from todo.views import addTodo
from todo.views import deleteTodo
from modelform.views import getUser
from imageUpload.views import *
from django.conf import settings
from django.conf.urls.static import static
#from imageUpload.views import imageUploadShow
#from imageUpload.views import imageUpload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', myview),
    path('todo/', todoView),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:item_id>/', deleteTodo),
    path('adduser/', getUser),
    path('uploadpaper/', paperUploadShow),
    path('filterPaper/', filterPaper),
    path('showPapers/<str:code>/', showPapers),
    path('showPapers/', showPapers)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
