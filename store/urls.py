from rest_framework_nested import routers

from . import views


router = routers.DefaultRouter()
router.register("applications", views.ApplicationViewSet, basename="application")


urlpatterns = router.urls