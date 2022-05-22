
from django.contrib import admin
from django.urls import path

from blog.views import blog_api, blog_detail_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blog/', blog_api.as_view()),
    path('api/blog/<int:pk>/', blog_detail_api.as_view())
]
