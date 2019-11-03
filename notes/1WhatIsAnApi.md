# [What is an API?](https://www.youtube.com/watch?v=RPsDhoWY_kc)

An API is an acronym for Application Programming Interface. 
**Application:** It's a functional app
**Programming:** It has an aspect of programming in it
**Interface:** An interface is like a facilitator of communication. So in the context of an 'API', an interface allows other users/machines/services to communicate with it.

### How does an API work?

An API only works with data. Data is transferred between any service that communicates with the API. These days APIs largely accept and return data in JSON or XML format. For example, if you wanted to fetch your user information from the server, the server would provide you with:

```json
{
    "email": "you@domain.com",
    "username": "yourusername"
}
```
### Why use/build an API?

There are many uses for an API and it depends on what your product/service is trying to achieve but mainly APIs are used to allow others to integrate with your product. This is attractive because integration allows for an enhanced product, or solves a problem that business cannot solve on its own.

As an example, one popular API would be:

[Stripe](https://stripe.com)

Stripe is an online payments handler and now taking on other services that helps run an online business. As an online business one of the challenges is to capture payments from your users. Stripe provides an API with a huge amount of functionality for capturing different kinds of payments, and hence solves one of the biggest problems an online business faces.

From a client perspective, Stripe solves a huge problem, and shows why an API can be so useful. From a developer perspective, building an API allows other developers easy access to integrate and use your product, which shows why building an API can be so powerful as a product/service.

With that being said, let's look at how Django can work as an API.

## Code:

- Create an app
```bash 
python manage.py startapp core 
```
- Inside the views of this app do the following

    ```python

    from django.http  import JsonResponse

    def test_view(request):
        data = {
            'name': 'John',
            'age': 23
        }
        return JsonResponse(data) 
        
        # return JsonResponse(data, safe =false) 
        # to pass something other than json data
    ```
- Here we have imported the JsonResponse
- test_view() takes request argument and return a Json data. Which is possible due to built in JsonResponse module in *django.http*
- to return something other than json data use safe=false argument.

- In root URL configuration: 

    ```python

    from core.views import test_view

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('',test_view,name='test')
    ]

    ```
- migrate and runserver, You will get json payload in the homepage. Inspect the page and go to the network to see the response. You will see the data in network-> response
- Using curl in terminal.

    ```bash

    F:\python\django_rf\django_restframework>curl http://127.0.0.1:8000
    {"name": "John", "age": 23}

    ```

- If we are working with post and have a postlistview and we would return all of our post in a json payload where each post would be its own **dictionary** and it would have all of the field of the model populated inside. Like title, description etc. all of that will be represented as dictionary and converted into a json payload. 
- Same thing for creating if you have create view and retrieving an instance if you have detail view and updating and deleting. 
- This is where django restframework comes in. 


### DRF:

The Django Rest Framework (DRF) is a package for building APIs with Django. It is one of the most well known Django packages and extremely powerful.

- Install DRF -> ```bash pip install djangorestframework ```
- pip freeze > requirements.txt
- Go to views and import the third party packages:

    ```python

    from rest_framework.response import Response
    from rest_framework.views import APIView


    class TestView(APIView):
        def get(self, request, *args, **kwargs):
            data = {
                'name': 'john',
                'age': 23
            }    
            return Response(data)

    ```
- Go to urls and makes the following changes:

    ```python

    from core.views import TestView

    urlpatterns = [
        path('api-auth/', include('rest_framework.urls')
        path('admin/', admin.site.urls),
        path('',TestView.as_view(),name='test')
        # path('',test_view,name='test')
    ]

    ```
- In the setting.py add restframework in the installed_apps

    ```python

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework' # Added portion
    ]

    ```

Here we import the Response from the DRF's response module, as well as the APIView, one of the DRF's wrappers for creating an API endpoint. Using these together we can create a simple endpoint that online accepts GET requests, and returns the dictionary of data as we saw before.

Please note that this is only scraping the surface of what the DRF provides. Among views and responses it provides functionality for explicitly defining authentication, permissions, and works so brilliantly with our Django models.