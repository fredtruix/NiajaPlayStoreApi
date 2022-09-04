from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import User_details, User_favorite, User_followers


class User_detailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_details
        fields = '__all__'


class User_followersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_followers
        fields = '__all__'



class User_favouriteSerializer(serializers.ModelSerializer):


    class Meta:
        model = User_favorite
        fields = '__all__'