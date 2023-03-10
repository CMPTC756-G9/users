from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User

# class UserSerializer(serializers.Serializer):
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     username = serializers.CharField()
#     password = serializers.CharField()
#     email = serializers.EmailField()


    # def update(self, instance, validated_data):
    #     for k, v in validated_data.items():
    #         if hasattr(instance, k):
    #             setattr(instance, k, v)
    #         else:
    #             raise ValidationError(detail=f'User does not have the attribute: {k}')
    #     instance.save()
    #     return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'slug'
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'email')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('password', '')
        return data