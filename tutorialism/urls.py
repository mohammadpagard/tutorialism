from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # root path
    path('', include('home.urls', namespace='home')),

    path('courses/', include('course.urls', namespace='course')),
    path('category/', include('category.urls', namespace='category')),
    path('video/', include('video.urls', namespace='video')),
    # ckeditor file path
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
