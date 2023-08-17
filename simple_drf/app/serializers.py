from rest_framework import serializers
from .models import Book
class TestSerizlizer(serializers.Serializer):
   name      = serializers.CharField(max_length = 50)
   email     = serializers.CharField( max_length=50)
   create_at = serializers.DateTimeField()
   id        = serializers.IntegerField()


class UserSerlizer(serializers.Serializer):
   username = serializers.CharField(required = True)
   email    = serializers.EmailField(required = True)
   password = serializers.CharField(required = True, write_only = True)
   
   def validate_username(self, value):
      if value == 'amiramir':
         raise serializers.ValidationError(" USER can't be amiramir ")
      return value
   

class BookSerilizer(serializers.ModelSerializer):
   class  Meta:
      model = Book
      fields = '__all__'
      extra_kwargs = {
         'price' : {'write_only' : True},
      }
   def validate_name(self, value):
      if value == "amir":
         raise serializers.ValidationError(" Simple validator ! ")
      return value
      # fields = ('name')
      # excludes = ('name')
    