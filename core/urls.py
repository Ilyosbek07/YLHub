from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('course/', include('apps.course.urls')),
    path('users/', include('apps.users.urls')),
    path('tests/', include('apps.tests.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("happenings/", include('apps.happenings.urls')),
    path("webinar/", include('apps.webinar.urls')),
    path("library/", include('apps.library.urls'))
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
