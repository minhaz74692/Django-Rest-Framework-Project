from rest_framework import serializers
from userapp.models import Users
from django.contrib.auth.models import User

from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', )

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError("Invalid login credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")

        data['user'] = user
        return data
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    # def validate(self, data):
    #     if len(data["password"])<6:
    #         raise serializers.ValidationError({"error": "Password must be more then 6 characters"})
        