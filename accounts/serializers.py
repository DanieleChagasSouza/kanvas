from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account


class AccoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "username", "password", "email", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}

    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=Account.objects.all(),
                message="A user with that username already exists.",
            )
        ],
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=Account.objects.all(),
                message="user with this email already exists.",
            )
        ],
    )

    def create(self, validated_data: dict) -> Account:
        if validated_data.get("is_superuser"):
            return Account.objects.create_superuser(**validated_data)
        else:
            return Account.objects.create_user(**validated_data)
