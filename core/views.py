from django.shortcuts import render
from django.http  import JsonResponse

# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializers contents:
from .serializers import PostSerializer
from .models import Post




class TestView(APIView):
     
    # --------Old Get without DRF--------

    # def get(self, request, *args, **kwargs):
    #     data = {
    #         'name': 'john',
    #         'age': 23
    #     }    
    #     return Response(data)

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        post = qs.first()
        # serializer = PostSerializer(qs, many=True)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



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