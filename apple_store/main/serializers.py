from rest_framework import serializers
from .models import *


class MainCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MainProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class MainCardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


