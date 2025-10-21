
from students.models import Student
from api.serializers import studentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET', 'POST'])  # allow GET and POST requests
def students(request):
    # This is manual method of serialization of QuerySet to list (Dictionary to JSON)
    # """ students = Student.objects.all()
    # students_list = list(students.values())
    # return JsonResponse(students_list, safe=False) """
    # Other Method: Using Serializer to get list from dictionaries
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = studentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':  # Deserialize or Creating a new Student using Serializer that model
        serializer = studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
#safe=False --> explanation:
JsonResponse has a safe parameter that defaults to True.
When safe=True, only dictionaries are allowed.
Setting safe=False tells Django it's okay to serialize other types like lists.
'''


@api_view(['GET', 'PUT', 'DELETE'])  # allow GET, PUT and DELETE requests
def studentView(request, pk):
    try:
        student = Student.objects.get(pk=pk)  # getting single student details

    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = studentSerializer(student)
    if request.method == 'GET':
        serializer = studentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update student details
    elif request.method == 'PUT':
        serializer = studentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Delete student details
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
