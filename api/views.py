
from students.models import Student
from api.serializers import studentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])  # only GET requests are allowed
def students(request):
    # This is manual serialization of QuerySet to list of dictionaries
    # """students = Student.objects.all()
    # students_list = list(students.values())
    # return JsonResponse(students_list, safe=False)"""
    # Other Method: Using Serializer to get list of dictionaries directly
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = studentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


'''
#safe=False --> explanation:
JsonResponse has a safe parameter that defaults to True.
When safe=True, only dictionaries are allowed.
Setting safe=False tells Django it's okay to serialize other types like lists.
'''
