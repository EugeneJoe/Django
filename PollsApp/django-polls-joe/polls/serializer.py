from rest_framework import serializers
from . import models


class Question_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = '__all__'


class Choice_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Choice
        fields = ['choice_text', 'votes']
