from src import views
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

router = DefaultRouter()
router.register('', views.EventViewset , basename='event')
urlpatterns = router.urls