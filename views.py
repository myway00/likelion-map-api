from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import serializers, mixins
# ListModelMixin 사용 위해 mixins 추가

from blog.models import Post

#blog_api 위에 정의해주세요!
class PostSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Post
        fields = '__all__'

class blog_api(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin ):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs) :
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class blog_detail_api(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)