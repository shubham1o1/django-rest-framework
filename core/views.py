from django.shortcuts import render
from django.http  import JsonResponse

# third party imports
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

# Serializers contents:
from .serializers import PostSerializer
from .models import Post


class PostView(mixins.ListModelMixin, 
                mixins.CreateModelMixin,
                generics.GenericAPIView,
                ):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     #send an email
    #     serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# class TestView(APIView):
     
#     permission_classes = (IsAuthenticated,)
    
#     # --------Old Get without DRF--------

#     # def get(self, request, *args, **kwargs):
#     #     data = {
#     #         'name': 'john',
#     #         'age': 23
#     #     }    
#     #     return Response(data)

#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         post = qs.first()
#         # serializer = PostSerializer(qs, many=True)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)



''' 
----------- v-1 API -----------

def test_view(request):
    data = {
        'name': 'John',
        'age': 23
    }
    return JsonResponse(data) 
    
    # return JsonResponse(data, safe =false) 
    # to pass something other than json data
'''