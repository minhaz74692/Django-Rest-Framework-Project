from rest_framework import serializers
from userapp.models import Users

class UserSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=20,)
    # email = serializers.CharField(max_length=40, )
    # phone = serializers.CharField(max_length=12, )
    # password = serializers.CharField(max_length=30,)
    class Meta:
        model = Users
        fields = '__all__'
    
    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.phone = validated_data.get("email", instance.phone)

    #     return instance