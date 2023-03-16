from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    def create(self, validate_data: dict) -> User:
        return User.objects.create_superuser(**validate_data)
    
    def update(self, instance: User, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()

        return instance

    class Meta:
        model = User
        field = [
            "id",
            "username",
            "email",
            "password",
            "is_superuser"    
        ]
        extra_kwargs = {"password":{"write_only":True}}
        read_only_field = [
            "id",
            "is_superuser"
        ]