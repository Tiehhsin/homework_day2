from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework import serializers
from api.serializers import TeacherSerializer, TeacherDeSerializer

from api.models import Student, Teacher


@method_decorator(csrf_exempt,name="dispatch")
class UserView(View):
    def get(self, request, *args, **kwargs):
        print("GET success")
        s = request.GET.get('username')
        print(s)
        return HttpResponse("GET ok")

    def post(self, request, *args, **kwargs):
        print("POST success")
        return HttpResponse("POST ok")

# Create your views here.
class StudentAPIView(APIView):
    # renderer_classes = [BrowsableAPIRenderer]
    # parser_classes = (JSONParser,)
    def get(self, request, *args, **kwargs):
        print("GET success")
        #request._request是原生的django请求,该请求作为一个属性
        #request是DRF的请求

        #wsgi的request
        # print(request._request.GET.get("email"))#不推荐
        #restframe_work.views.Request
        # print(request.GET.get('email'))
        # s = request.query_params
        # print(s,type(s))
        # s = request.data
        # print(s,type(s))
        print(request.data,'drf的方法')

        stu_id = kwargs.get("id")
        stu_obj = Student.objects.get(pk=stu_id)
        print(stu_obj)

        return Response("GET ok")

    def post(self, request, *args, **kwargs):
        print("POST success")
        print(request._request.POST.get('email'))#不能接收json类型,其他的就算解析器注掉了也能拿到
        print(request.POST.get('email'),11111)
        print(request.data)
        return Response("POST ok")

    # def exception_handler(self):

class TeacherAPIView(APIView):
    def get(self,request,*args,**kwargs):
        tea_id = kwargs.get("id")
        print(tea_id)
        if tea_id:

            # s = Teacher.objects.filter(pk=tea_id).values("username","password")
            # print(s)

            tea_obj = Teacher.objects.get(pk=tea_id)
            tea_serializer = TeacherSerializer(tea_obj).data
            return Response({
                "status":200,
                "message":"查询单个教师成功!",
                "result": tea_serializer
            })
        else:
            Teacher_objects_all = Teacher.objects.all()
            teach_serializer = TeacherSerializer(Teacher_objects_all,many=True).data
            return Response({
                "status": 200,
                "message": "查询所有教师成功!",
                "result": teach_serializer
            })
    def post(self,request,*args,**kwargs):
        request_data = request.data
        print(request_data,"124568")
        if not isinstance(request_data,dict) or request_data == {}:
            return Response({
                "status":400,
                "message":"参数有误",
            })
        serializer = TeacherDeSerializer(data=request_data)
        if serializer.is_valid():
            tea_ser = serializer.save()
            print(tea_ser)
            return Response({
                "status":200,
                "message":"员工添加成功",
                "results": TeacherSerializer(tea_ser).data
            })
        else:
            return Response({
                "status": 400,
                "message": "教师添加失败",
                # 保存失败的信息会包含在 .errors中
                "results": serializer.errors
            })
