from rest_framework import serializers
from src.models import *
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    # name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['_id', 'name', 'branch', 'regno','isAdmin','username']
    
    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    # def get_name(self, obj):
    #     print("Object is=> ",obj.first_name)
    #     name = obj.first_name
    #     if name == '':
    #         name = obj.name

    #     return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['_id', 'name', 'branch', 'regno','token']


    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)




class EventSerializer(serializers.ModelSerializer):

    # club_name=UserSerializer(many=True)
    class Meta:
        model = event
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    team_members=UserSerializer(many=True)
    contributor=UserSerializer(many=False)

    class Meta:
        model = project
        fields = '__all__'


class FeedSerializer(serializers.ModelSerializer):
    team_members=UserSerializer(many=True)
    contributor=UserSerializer(many=False)

    class Meta:
        model = feed
        fields = '__all__'