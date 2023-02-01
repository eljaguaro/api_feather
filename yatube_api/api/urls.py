from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter


app_name = 'api'

router = DefaultRouter()

router.register('posts', views.PostViewSet)
router.register('groups', views.GroupViewSet)
router.register((r'posts/(?P<post_id>\d+)/comments'),
                views.CommentViewSet, basename='comment')


urlpatterns = [
    path('', include(router.urls))
]
