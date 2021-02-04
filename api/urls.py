from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url("courses",views.CourseApiView.as_view()), 
    url("users",views.UserApiView.as_view()), 
    url("lectures",views.LectureApiView.as_view()), 
]