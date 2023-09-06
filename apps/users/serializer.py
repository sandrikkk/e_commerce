from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    isAdmin = serializers.ReadOnlyField(source='is_staff')
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        extra_kwargs = {"password": {"write_only": True}}
        fields = (
            'id',
            'email',
            'username',
            'is_verified',
            'isAdmin',
            'role',
            'password',
            'password_confirm'
        )

    def validate(self, attrs):
        attrs = super().validate(attrs)
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Passwords do not match.')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
