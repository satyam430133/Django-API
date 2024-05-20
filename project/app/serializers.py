from rest_framework import serializers
from .models import *

class StulistSerializer(serializers.ModelSerializer):
    class Meta():
        model = StuModel
        fields = "__all__"