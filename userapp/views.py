from django.shortcuts import render
from rest_framework.decorators import api_view
from userapp.models import Users
from userapp.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.authtoken.models import Token

# Class Based Django Views
class UserRegistration(APIView):
    def post(self, request):
        name = request.data['name']
        email = request.data['email']
        phone = request.data['phone']
        password = request.data['password']


        userList = Users.objects.all()
        exist =  any(item.email == email for item in userList)
        if exist: 
            return Response({"Exist": "This email is already exist"})

        userSerializer = UserSerializer()
        userSerializer.validate(request.data)


        get_data = Users.objects.create(
            name = name, email = email, phone = phone, password = password,
        )
        serializer = UserSerializer(get_data, many = False)
        print("Response Data: ", serializer.data)
        if serializer.data:
            user = Users.objects.get(id = serializer.data["id"])

            # print("User", user)
            # print("User", str(user))

            token_obj , _ = Token.objects.get_or_create(user = serializer)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
    
class UserList(APIView):
    def get(self, request):
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

                serializer = UserSerializer(users, many = True)
                return Response(userData, status= status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserDetails(APIView):
    def get_data(self, pk):
        try:
           return Users.objects.get(id=pk)
        except Users.DoesNotExist:
            raise Http404
        

    def get(self, request, pk ):
        serializer = UserSerializer(self.get_data(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_data(pk)
        if request.data:
            try:
                if 'name' in request.data and 'phone' in request.data:
                    user.name = request.data['name']
                    user.phone = request.data['phone']
                    user.save()

                    serializer = UserSerializer(user)
                    if serializer.data:
                        return Response(serializer.data)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"message": "Both 'name' and 'phone' fields are required."}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"message": "Something went wrong!", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        user = self.get_data(pk)
        user.delete()
        return Response({"message": "User Deleted Successfully!!"},status=status.HTTP_204_NO_CONTENT)















# Function based django views
# Create your views here.
# @api_view(['GET', 'POST'])
# def user_list(request, format = None):
#     # userSerializer = UserSerializer()

#     if request.method == "GET":
#         users = Users.objects.all().order_by('id') #use '-id' for descending order return
#         # serializer = UserSerializer({}, many = False)
#         if users:
#             userData = []
#             for user in users:
#                 emptyMap = {}
#                 emptyMap['id'] = user.id
#                 emptyMap['name'] = user.name
#                 emptyMap['email'] = user.email
#                 emptyMap['phone'] = user.phone
#                 emptyMap['password'] = user.password
#                 userData.append(emptyMap)

#             serializer = UserSerializer(users, many = True)
#             return Response(userData, status= status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == "POST":
#         name = request.data['name']
#         email = request.data['email']
#         phone = request.data['phone']
#         password = request.data['password']


#         get_data = Users.objects.create(
#             name = name, email = email, phone = phone, password = password,
#         )
#         serializer = UserSerializer(get_data, many = False)
#         if serializer.data:
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#         # serializer = UserSerializer(data=request.data)
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data, status = status.HTTP_201_CREATED)
#         # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(["GET", "PUT", "DELETE"])
# def user_details(request,pk, format = None):
#     users = Users.objects.all()
#     try:
#         user = Users.objects.get(id=pk)
#     except Users.DoesNotExist:
#         return Response({"message": "No user found with this ID!"},status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
    
#     elif request.method == "PUT":
#         if request.data:
#             try:
#                 if 'name' in request.data and 'phone' in request.data:
#                     user.name = request.data['name']
#                     user.phone = request.data['phone']
#                     user.save()

#                     serializer = UserSerializer(user)
#                     if serializer.data:
#                         return Response(serializer.data)
#                     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#                 else:
#                     return Response({"message": "Both 'name' and 'phone' fields are required."}, status=status.HTTP_400_BAD_REQUEST)
#             except Exception as e:
#                 return Response({"message": "Something went wrong!", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
#     elif request.method == 'DELETE':
#         user.delete()

#         return Response({"message": "User Deleted Successfully!!"},status=status.HTTP_204_NO_CONTENT)