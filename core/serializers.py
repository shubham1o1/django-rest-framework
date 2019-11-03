from rest_framework import serializers

from .models import Post


'''
    -----------------------------------
    |        similar to forms         |
    -----------------------------------

    from django import forms

    class postForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = (
                'title','description'
            )
'''

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'owner'
        )
