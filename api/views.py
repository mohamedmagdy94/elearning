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
            for course in allCourses:
                course.request_count += 1
                course.save()
        data = serializers.serialize('json', allCourses)
        return HttpResponse(data, content_type="application/json")
    def post(self,request):
        course=Course(identifier=0,course_title=request.POST['course_title'],num_subscribers=0,subject=request.POST['subject'])
        course=Course(identifier=0,course_title=request.POST['course_title'],num_subscribers=0,subject=request.POST['subject'],request_count=0)
        allCourses=Course.objects.all()
        coursesSorted = merge_sort(allCourses, 0, len(allCourses) -1, lambda firstCourse, secondCourse: firstCourse.request_count > secondCourse.request_count)
        coursesSorted.save()
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



def merge(array, left_index, right_index, middle, comparison_function):
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # We use the comparison_function instead of a simple comparison operator
        if comparison_function(left_copy[left_copy_index], right_copy[right_copy_index]):
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        sorted_index = sorted_index + 1

    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


def merge_sort(array, left_index, right_index, comparison_function):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(array, left_index, middle, comparison_function)
    merge_sort(array, middle + 1, right_index, comparison_function)
    merge(array, left_index, right_index, middle, comparison_function)    