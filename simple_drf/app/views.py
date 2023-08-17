from rest_framework.response import Response




from rest_framework.decorators import api_view
@api_view()
def hello_world(request):
    return Response({"message": "Hello, world! with decorators"})
 
 

from rest_framework.views import APIView
from .serializers import TestSerizlizer, UserSerlizer
from .models import Test
from django.contrib.auth.models import User

class MyClass(APIView):

   def post(self, request):
      user = UserSerlizer(data = request.POST)
      if user.is_valid():
         User.objects.create_user(
            username = user.validated_data["username"],
            email = user.validated_data["email"],
            password = user.validated_data["password"],
         )
         return Response(user.data)
      return Response(user.errors)
      
   
   def get(self, request):
      test = Test.objects.all()
      data = TestSerizlizer(instance = test, many = True )
      return Response(data = data.data)