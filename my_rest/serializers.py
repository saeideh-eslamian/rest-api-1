from rest_framework import serializers
from .models import Articel

class ArticelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articel
        fields = "__all__"
        # fields = ['id','name', 'auther', 'description', 'date']