# cases/urls.py
from rest_framework.routers import DefaultRouter
from .views import CaseViewSet

router = DefaultRouter()
router.register(r'cases', CaseViewSet)

urlpatterns = router.urls
