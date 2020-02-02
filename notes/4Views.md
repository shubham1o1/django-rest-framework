# Views:

- APIView is a simplest wrapper that we can use to create an API endpoint. It is provided by DRF
- We specify the method we want to handle such as get requests or post requests. And the logic that takes place when we recieve the request for that particular method. 
- Our code for APIView and it's logic looks as follows:
```python

class TestView(APIView):

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

```
- As we explore more views we will see that they get more and more abstracted. It allows us to write lot less code while achieving the same goal.
- This section is mostly about the level of abstraction that comes with inheritance and generic classes of Views available. 
- 
