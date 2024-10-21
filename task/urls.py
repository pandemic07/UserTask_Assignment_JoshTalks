from rest_framework.routers import DefaultRouter
from .api import TaskViewSet, UserViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet)
router.register(r"users", UserViewSet)

urlpatterns = router.urls
