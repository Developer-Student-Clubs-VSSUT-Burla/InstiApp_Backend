from src import views
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

router = DefaultRouter()
router.register('', views.FeedViewSet , basename='feed')
urlpatterns = router.urls