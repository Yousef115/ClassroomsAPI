from rest_framework import serializers
from classes.models import Classroom

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['subject', 'year', 'teacher',]


class ClassroomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'


class ClassroomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        exclude=['teacher']