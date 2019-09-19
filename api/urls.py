from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'accounts', views.AccountViewSet)
router.register(r'companies', views.CompanyViewSet)

urlpatterns = router.urls
