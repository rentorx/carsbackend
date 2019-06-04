from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'accounts', views.AccountViewSet)

urlpatterns = router.urls
