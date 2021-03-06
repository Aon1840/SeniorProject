from rest_framework import serializers
from Users.models import User

# class UserSerializer(serializers.Serializer):
#     user_id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(required=True,allow_blank=False,max_length=15)
#     password = serializers.CharField(required=True,allow_blank=False,max_length=20)
#     name = serializers.CharField(required=True,allow_blank=False,max_length=30)
#     surname = serializers.CharField(required=True,allow_blank=False,max_length=30)
#     tel = serializers.CharField(required=True,allow_blank=False,max_length=10)
#     email = serializers.EmailField(required=True,allow_blank=False)
#     register_date = serializers.DateTimeField(read_only=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id','username','password','name','surname','tel','email','register_date')

    def create(self, validated_data):
        #method for create and return new 'User' instance
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #method for update and return exist 'User' instance
        instance.username = validated_data.get('username',instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.tel = validated_data.get('tel', instance.tel)
        instance.email = validated_data.get('email', instance.email)

        instance.save()
        return instance