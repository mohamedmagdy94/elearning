from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
# from .serializers import *
from django.core import serializers
from rest_framework import viewsets
import json
from bson import ObjectId
from django.http import JsonResponse
from django.http import HttpResponse
import logging




class CourseApiView(APIView):
    def get(self,request):
        query = request.GET.get('query')
        if query is None:
            allCourses=Course.objects.all()
        else:
            allCourses=Course.objects.filter(course_title=query)
        data = serializers.serialize('json', allCourses)
        return HttpResponse(data, content_type="application/json")
    def post(self,request):
        course=Course(identifier=0,course_title=request.POST['course_title'],num_subscribers=0,subject=request.POST['subject'])
        course.save()
        return HttpResponse('')    
    def delete(self,request):
        course=Course.objects.filter(course_title=query).first()
        course.delete()
        return HttpResponse('')    

class UserApiView(APIView):
    def get(self,request):
        email = request.GET.get('email')
        password = request.GET.get('password')
        users=User.objects.filter(email=email,password=password)
        if len(users) > 0:
            return HttpResponse('',status=200)    
        else:
            return HttpResponse('',status=401)    
        
    def post(self,request):
        user=User(email=request.POST['email'],password=request.POST['password'],role=1)
        user.save()
        return HttpResponse('')    

class LectureApiView(APIView):
    def get(self,request):
        course_title = request.POST.get('course_title')
        lectures = Lecture.objects.all()
        data = serializers.serialize('json', lectures)
        return HttpResponse(data, content_type="application/json")

    def post(self,request):
        title = request.POST.get('title')
        subject = request.POST.get('subject')
        attachment = request.POST.get('attachment')
        course_title = request.POST.get('course_title')
        lecture = Lecture(title=title,subject=subject,attachment=attachment,courses=[])
        lecture.save()
        return HttpResponse('')    



    