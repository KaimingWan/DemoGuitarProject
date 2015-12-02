from django.conf.urls import include, url

__author__ = 'Kami Wan'

urlpatterns = [

    url(r'^summernote/', include('django_summernote.urls')),  # summernote插件
]
