from rest_framework import serializers
from userapp.models import Users
from django.contrib.auth.models import User

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
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    # def validate(self, data):
    #     if len(data["password"])<6:
    #         raise serializers.ValidationError({"error": "Password must be more then 6 characters"})
        