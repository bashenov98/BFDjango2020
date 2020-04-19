from rest_framework import serializers

from auth_.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'is_superuser', 'password',)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(username=validated_data['username'])

        user.set_password(validated_data['password'])

        user.save()

        return user