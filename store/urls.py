from rest_framework_nested import routers

from . import views


router = routers.DefaultRouter()
router.register("applications", views.ApplicationViewSet, basename="application")


services_router = routers.NestedDefaultRouter(router, "applications", lookup="application")
services_router.register("services", views.ServiceViewSet, basename="application-service")

comment_router = routers.NestedDefaultRouter(services_router, "services", lookup="service")
comment_router.register("comments", views.CommentViewSet, basename="service-comment")


urlpatterns = router.urls + services_router.urls + comment_router.urls