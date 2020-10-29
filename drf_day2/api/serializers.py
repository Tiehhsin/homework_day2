from rest_framework import serializers

from api.models import Teacher
from drf_day2 import settings


class TeacherSerializer(serializers.Serializer):
    #定义序列化器类
    username = serializers.CharField()
    password = serializers.CharField()
    # gender = serializers.IntegerField()
    phone = serializers.CharField()
    # pic = serializers.ImageField()
    gender = serializers.SerializerMethodField()
    pic = serializers.SerializerMethodField()


    def get_gender(self,obj):
        print(obj.get_gender_display())
        return obj.get_gender_display()

    def get_pic(self,obj):
        return "%s %s %s"%("http://127.0.0.1:8000/",settings.MEDIA_URL,str(obj.pic))



class TeacherDeSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=3,
        min_length=2,
        error_messages={
            "max_length":"过于长",
            "min_length":"过于短",
        }
    )
    password = serializers.CharField()
    phone = serializers.CharField()
    gender = serializers.IntegerField()
    # pic = serializers.ImageField()
    def create(self, validated_data):
        print(self,validated_data)
        return Teacher.objects.create(**validated_data)