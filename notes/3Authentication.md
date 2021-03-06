# Authentication: 

- Protects the API endpoints using DRF permission.
- Third party packages DRF recommends
- Import options:

    ```python 
    from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly 
    ```
- Specify in our api view
    ```python
    class TestView(APIView):
        
        permission_classes = (IsAuthenticated,)
        ...
    ```
- permission_classes could be a list or a tupule.
- What its basically means is that no matter which method we are sending as a request (post, get, and so on) we will need to be authenticated  for the view to handle our requests. Otherwise we will get unauthenticated error. 
- If we try to access without authentication we get the following error:
    ![Forbidden 403](ss/PMunAuthenticated.JPG)
- TestView handles the localhost and the get/post method. Trying to access testview without being authenticated lead to above error. 

## How to authenticate our users:


### In projects setting:
- In the bottom add the following
    ```python
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication'
        ]
    }
    ```
- REST_FRAMEWORK is a dictionary where we specify a key that represents keys in the DRF.
- 'DEFAULT_AUTHENTICATION_CLASSES' is a list of classes that we can apply. 
- 'rest_framework.authentication.TokenAuthentication' is one way of authenticating our users. Default django uses basic authentication as well as session authentication. 
- If you are logged in as admin then it is going to use session to see if your user is authenticated and that session is stored normally through cookies in the browser. Whereas token authentication works little bit differently. Every time you create a user or log in your token is refreshed and that token is kind of like your API key that allows you to send requests instead of needing to pass your username and password every single time you would then just use that token to authenticate yourself.
- So in order to use this we need to go into installed apps and add following:
    ```python
    INSTALLED_APPS = [
        ...
        'rest_framework.authtoken'
    ]
    ```
- We must now add migration.
    ```bash
    Apply all migrations: admin, auth, authtoken, contenttypes, core, sessions
    Running migrations:
    Applying authtoken.0001_initial... OK
    Applying authtoken.0002_auto_20160226_1747... OK
    ```
- Now create superuser and run the server, log in to the admin. Token section appears in the database.

### Creating token:
    ```bash
    python manage.py drf_create_token admin
    ```
    - Creates token for user admin
- Copy token, go to postman, authorization, choose API Key, Specify key and value
- Authorization is the key, copied token is the value.
- If we send we get the record back:
 ![Passing Token](ss/PMpassingToken.JPG)
- Go to code -> python -> request to see the code
 ![python code](ss/PMpythonCode.JPG)
 - We are passing authorization as key in our header as:
    ```bash
    headers = {
        'Authorization': "Token cc9c80b4b5430a20a6a87dba5b836b57d3e92d82",
        ...
    ```
- When we have a frontend (react/angular/..) and our app has the login page we will need to fill in username and password send them off and then need the token user returned back to us.
- Right now we are grabbing the token. But we must rather supply it to the user when they log in. 

### views and urls in token generation:

- go to views
- add view in url, that comes directly from django rest framework
- In urls.py of the core app you do the following:
```python 
    ...
    from rest_framework.authtoken.views import obtain_auth_token 
    ...

    urlPatterns = [
        ...
        path('api/token/', obtain_auth_token, name = 'obtain-token'),
    ]
```
- obtain_auth_token is a view that will return token for a user when we send user name and password. 
- path -> to send our token to : ```'api/token/'```
- view that handle the logic of sending the token: ```obtain_auth_token```
- the name of the token: ```'obtain-token'```
- In postman send the username and password to the following url and you get the token : ```localhost:8000/api/token```
![Getting Token for username and password](ss/PMsendingUsernameGettingToken.JPG)

- There are several third party packages tat DRF recommends to configure authentication
- Check out authentication in DRF documentation. 
- choices: django-rest-auth, Django REST framework OAuth, django-rest-framework-social-oauth2
- We are using django-rest-auth. Go to its documentation and see how to install: ```pip install django-rest-auth```
- in settings.py in INSTALLED_APPS, add : ```  'rest_auth', ```
- in urls.py add: 
```python
    path('rest-auth/', include('rest_auth.urls')),
```
- Run migrations
- Go to postman, open a new window, and type the address: ```localhost:8000/rest-auth/login/``` under POST request 
- Also, add pass the username and password as form data
- hit send, then you'll get a json response of some key and it's token value pair. 
![Third Party Magic](ss/PMrestAuthInBuiltView.JPG)

- You can do something similar for password reset, for forgot password. See API endpoints in rest-auth's documentation. 
- registration and all sorts of authentication are present. 
