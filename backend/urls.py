from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from rest_framework import routers

#Enrutador
router = routers.DefaultRouter()
router.register('Workers', views.WorkerViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    url(r'api/v1/format/Workers/(?P<pk>[0-9]+)/$', views.WorkerDetail.as_view()),

    path('api/v1/auth/', include('rest_auth.urls')),
    path('api/v1/auth/register/',  include('rest_auth.registration.urls')),
    path('api/v1/auth/accounts/', include('allauth.urls')),
]
