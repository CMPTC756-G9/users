from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'username'
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'email')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('password', '')
        return data
