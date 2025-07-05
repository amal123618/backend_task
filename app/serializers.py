from rest_framework import serializers
from .models import User
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'mobile_number']

    def validate_name(self, value):
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError("Name should only contain letters and spaces.")
        return value.strip()

    def validate_mobile_number(self, value):
        if not re.match(r'^[6-9]\d{9}$', value):
            raise serializers.ValidationError("Enter a valid 10-digit Indian mobile number starting with 6-9.")
        return value

    def validate(self, data):
        name = data.get('name')
        mobile_number = data.get('mobile_number')
        if User.objects.filter(name=name, mobile_number=mobile_number).exists():
            raise serializers.ValidationError("A user with this name and mobile number already exists.")
        return data
