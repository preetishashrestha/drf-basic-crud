from rest_framework import serializers
from .models import Student
import re
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField()
    phone=serializers.CharField()
    message=serializers.CharField()

    def create(self, validate_data):
        return Student.objects.create(**validate_data)
    
    def validate_age(self, age):
        if age<0 or age>=100:
            raise serializers.ValidationError("age should be between 0 to 100")
        return age

    def validate_phone(self, phone):
        if not re.match(r"^(98|97)\d{8}$",phone):
            raise serializers.ValidationError("invalid Phone")
        return phone
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get("name", instance.name) # instance.name means old name will be saved if nothng is there
        instance.age=validated_data.get("age", instance.age)
        instance.phone=validated_data.get("phone", instance.phone)
        instance.message=validated_data.get("message", instance.message)
        instance.save()
        return instance
        