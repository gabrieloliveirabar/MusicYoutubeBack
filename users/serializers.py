from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = [
            "id",
        ]
        depth = 1

    def create(self, validated_data: dict) -> User:
        if validated_data["is_superuser"] == True:
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()

        return instance
