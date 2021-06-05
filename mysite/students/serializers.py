#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Student


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


# 字段验证函数
def check_sex_value(data):
    if data not in [1, 0]:
        raise serializers.ValidationError("sex value only have 1 and 0")


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="ID", read_only=True)
    name = serializers.CharField(label="名称", max_length=20, required=True)
    sex = serializers.IntegerField(label="性别", required=False, allow_null=True, validators=[check_sex_value])
    age = serializers.IntegerField(label="年龄", required=True)
    description = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    def validate_name(self, attr):
        print(f"attr:{attr}")
        if attr == "老鹰":
            raise serializers.ValidationError("对不起你太凶了")
        return attr

    def validate(self, attrs):
        print(attrs)
        if attrs.get("age") > 60 and attrs.get("sex") == 1:
            raise serializers.ValidationError("对不起男人的年龄不能超过60")
        return attrs

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
