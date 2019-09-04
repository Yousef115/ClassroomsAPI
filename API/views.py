from django.shortcuts import render
from rest_framework.generics import (ListAPIView, RetrieveAPIView, 
	RetrieveUpdateAPIView, CreateAPIView, DestroyAPIView)
from django.contrib.auth.models import User

from .serializers import ClassroomSerializer, ClassroomCreateSerializer, ClassroomDetailSerializer
from classes.models import Classroom

# Create your views here.

class ClassroomList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomSerializer


class ClassroomDetail(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassroomCreate(CreateAPIView):
	serializer_class = ClassroomCreateSerializer

	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)


class ClassroomUpdate(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomCreateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassroomDelete(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'