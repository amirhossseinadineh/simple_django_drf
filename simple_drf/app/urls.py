from django.urls    import path
from .              import views

urlpatterns =[
    path('',               views.hello_world,              name = 'main'),
    path('class',         views.MyClass.as_view(),              name = 'class'),


]