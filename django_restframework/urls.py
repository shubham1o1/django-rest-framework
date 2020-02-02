from django.contrib import admin
from django.urls import path, include
# from core.views import test_view
from core.views import PostView, PostCreateView, PostListCreateView

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
    path('',PostView.as_view(),name='test'),
    path('create/',PostCreateView.as_view(),name='create'),
    path('list-create/',PostListCreateView.as_view(),name='list-create'),
    # path('',test_view,name='test')
    path('api/token/', obtain_auth_token, name = 'obtain-token'),

]
