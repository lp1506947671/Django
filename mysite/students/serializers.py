#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Student


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    sex = serializers.BooleanField()
    age = serializers.IntegerField()
    description = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
