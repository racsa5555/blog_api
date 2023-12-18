from django.contrib.auth.models import User
from rest_framework import serializers
class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required = True)
    last_name = serializers.CharField(required = True)
    password = serializers.CharField(required = True, min_length = 8,write_only = True)
    password_confirmation = serializers.CharField(required = True, min_length = 8,write_only = True)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','password','password_confirmation']

    def validate(self, attrs):
        password_conf =attrs.pop('password_confirmation')
        if password_conf != attrs['password']:
            raise serializers.ValidationError('Пароли не совпадают')
        if not attrs['first_name'].istitle():
            raise serializers.ValidationError('Имя должно начинаться с заглавной буквы')
        return attrs
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
