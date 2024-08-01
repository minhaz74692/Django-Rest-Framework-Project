from django.shortcuts import render
from rest_framework.decorators import api_view
from userapp.models import Users
from userapp.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def user_list(request, format = None):
    # userSerializer = UserSerializer()

    if request.method == "GET":
        users = Users.objects.all().order_by('id') #use '-id' for descending order return
        # serializer = UserSerializer({}, many = False)
        if users:
            userData = []
            for user in users:
                emptyMap = {}
                emptyMap['id'] = user.id
                emptyMap['name'] = user.name
                emptyMap['email'] = user.email
                emptyMap['phone'] = user.phone
                emptyMap['password'] = user.password
                userData.append(emptyMap)

            # serializer = UserSerializer(users, many = True)
            return Response(userData, status= status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "POST":
        name = request.data['name']
        email = request.data['email']
        phone = request.data['phone']
        password = request.data['password']


        get_data = Users.objects.create(
            name = name, email = email, phone = phone, password = password,
        )
        serializer = UserSerializer(get_data, many = False)
        if serializer.data:
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        # serializer = UserSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status = status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["Get", "PUT", "DELETE"])
def user_details(request, format = None):
    return "skldjflksjdf"