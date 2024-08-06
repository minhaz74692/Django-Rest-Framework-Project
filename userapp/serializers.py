from rest_framework import serializers
from userapp.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    def validate(self, data):
        if len(data["password"])<6:
            raise serializers.ValidationError({"error": "Password must be more then 6 characters"})