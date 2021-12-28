from django.http import HttpResponse

from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Marks, Student
from .serialize_data import \
    StuGetSerializer, MarksGetSerializer, MarksPostSerializer, StudentPostSerializer
from rest_framework.response import Response

class MarksTotal(APIView):

    def get(self, request):
        chk_marks = Marks.objects.all().order_by('stu_id')
        lm = len(chk_marks)
        if lm == 0:
            return HttpResponse("NO records found for marks")
        serialized_marks = MarksGetSerializer(chk_marks, many=True)
        print(serialized_marks)
        data = serialized_marks.data
        total = list()
        for cur in data:
            tot = dict()
            tot['stu_id'] = cur['stu_id']
            tot['total'] = sum(cur.values()) - cur['stu_id']
            total.append(tot)
        return Response(total)

class MarksAvg(APIView):

    def get(self, request):
        chk_marks = Marks.objects.all().order_by('stu_id')
        lm = len(chk_marks)
        if lm == 0:
            return HttpResponse("NO records found for marks")
        serialized_marks = MarksGetSerializer(chk_marks, many=True)
        print(serialized_marks)
        data = serialized_marks.data
        avg_marks = {'maths': 0, 'physics': 0, 'chemistry': 0, 'biology': 0, 'english': 0}
        for cur in data:
            avg_marks['maths'] += cur['maths']
            avg_marks['physics'] += cur['physics']
            avg_marks['chemistry'] += cur['chemistry']
            avg_marks['biology'] += cur['biology']
            avg_marks['english'] += cur['english']

        avg_marks['maths'] = avg_marks['maths'] // lm
        avg_marks['physics'] = avg_marks['physics'] // lm
        avg_marks['chemistry'] = avg_marks['chemistry'] // lm
        avg_marks['biology'] = avg_marks['biology'] // lm
        avg_marks['english'] = avg_marks['english'] // lm
        return Response(avg_marks)

class MarksView(APIView):

    def get(self, request, stu_id):
        chk_marks = Marks.objects.filter(stu_id=stu_id)
        # print(len(chk_marks))
        if len(chk_marks) == 1:
            mrk = (chk_marks[0])
            serialized_marks = MarksGetSerializer(mrk)
            return Response(serialized_marks.data)
        else:
            return HttpResponse("Marks data not found for student_id "+stu_id)
    def post(self, request, stu_id):

        # check existing marks data
        print("request.data :", request.data)
        serializer_data = MarksPostSerializer(data=request.data)
        if not serializer_data.is_valid():
            return HttpResponse("Invalid Input")
        # print("HHH", serializer_data)
        chk_marks = Marks.objects.filter(stu_id=stu_id)
        # print(len(chk_marks))
        if len(chk_marks) == 1:
            mrk = (chk_marks[0])
            # print(mrk)

            mrk.maths = request.data.get("maths", mrk.maths)
            # return HttpResponse("Hello, world. This is marks apps, marks added existing**")
            mrk.physics = request.data.get("physics", mrk.physics)

            mrk.chemistry = request.data.get("chemistry", mrk.chemistry)

            mrk.biology = request.data.get("biology", mrk.biology)

            mrk.english = request.data.get("english", mrk.english)
            mrk.save()
            serialized_marks = MarksGetSerializer(mrk)
            return Response({'data': serialized_marks.data,
                             'response': "Hello, world. This is marks apps, marks added existing"})
            return HttpResponse("Hello, world. This is marks apps, marks added existing**")
        # serialized_marks = MarksGetSerializer(chk_marks[0])
        # print(serialized_marks)
        # return Response(serialized_marks.data)
        # return HttpResponse("Hello, world. This is marks apps, marks added ret")
        stu = Student.objects.filter(id=stu_id)
        print('LENGTH', len(stu))
        if len(stu) == 0:
            return HttpResponse("Student record for student id "+stu_id+" does not exist")

        mrk = Marks()
        mrk.stu_id = stu[0]
        mrk.maths = request.data.get("maths", 0)
        # return HttpResponse("Hello, world. This is marks apps, marks added existing**")
        mrk.physics = request.data.get("physics", 0)

        mrk.chemistry = request.data.get("chemistry", 0)

        mrk.biology = request.data.get("biology", 0)

        mrk.english = request.data.get("english", 0)
        mrk.save()
        serialized_marks = MarksGetSerializer(mrk)
        return Response({'data': serialized_marks.data,
                        'response': "Hello, world. This is marks apps, marks added"})
        return HttpResponse("Hello, world. This is marks apps, marks added")