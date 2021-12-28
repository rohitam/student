from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Student
from .serialize_data import StuGetSerializer, StudentPostSerializer, MarksGetSerializer
from rest_framework.response import Response

class StuView(APIView):

    def post(self, request):
        # pass
        data = request.data
        serialized_data = StudentPostSerializer(data=data)
        if not serialized_data.is_valid():
            return HttpResponse("Invalid data")
        stu = Student.objects.create(name=data['name'],
                                     first_name=data['first_name'],
                                     last_name=data['last_name'],
                                     email=data['email'])
        serialized_stu = StuGetSerializer(stu)
        return Response({'data': serialized_stu.data,
                        'response': "Student record added"})

    def get(self, request):
        # stu = Student.objects.filter(id=4)
        stu = Student.objects.all()
        slr = StuGetSerializer(stu, many=True)

        # print(stu.get())
        # print(slr.data[0]['name'])
        print(slr.data)
        return Response(slr.data)

        return HttpResponse("Hello, world. This is marks apps|||")