from rest_framework import serializers
from .models import Marks, Student

class CustomSerializer(serializers.Serializer):

    def ui_repr(self):

        def get_error(element):

            if type(element) == list:
                return element[0]
            else:
                inner_res_str = ''
                for inner_key in element:
                    if not isinstance(inner_key, str) and not isinstance(inner_key, str):
                        str_key = 'element' + str(inner_key + 1)
                    else:
                        str_key = inner_key
                    inner_res_str += str_key + ': ' + str(get_error(element[inner_key]))
                return inner_res_str

        response_str = ''

        for key in self.errors:
            response_str += '\n' if response_str else ''

            response_str += key + ': ' + str(get_error(self.errors[key]))

        return response_str

class StuGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'email', 'id', 'first_name', 'last_name')

class MarksGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = ('stu_id', 'maths', 'physics', 'chemistry', 'biology', 'english')

class StudentPostSerializer(CustomSerializer):

    name = serializers.CharField(max_length=60)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=60)

class MarksPostSerializer(CustomSerializer):
    maths = serializers.IntegerField()
    physics = serializers.IntegerField()
    chemistry = serializers.IntegerField()
    biology = serializers.IntegerField()
    english = serializers.IntegerField()