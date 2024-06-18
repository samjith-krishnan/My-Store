from rest_framework import serializers
from api.models import Products,Carts,Review
from django.contrib.auth.models import User


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    category = serializers.CharField()
    image = serializers.ImageField

class ProductModelSerializer(serializers.ModelSerializer):
    avg_rating=serializers.CharField(read_only=True)
    count_review = serializers.CharField(read_only=True)
    class Meta:
        model = Products
        fields = "__all__"

        # fileds = ["name","price"]

class Userserializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']

    def create(self,validated_data):
        
        return User.objects.create_user(**validated_data)
    
class Cartserializer(serializers.ModelSerializer):

    id = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    product = serializers.CharField(read_only=True)
    date = serializers.CharField(read_only=True)

    class Meta:

        model =  Carts
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    product =serializers.CharField(read_only = True)
    user = serializers.CharField(read_only = True)
    

    class Meta:
        model = Review
        fields = "__all__"
