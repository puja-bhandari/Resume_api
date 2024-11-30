from rest_framework import serializers
from . models import resumeHome

class resumeHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = resumeHome
        fields= "__all__"