from rest_framework.routers import DefaultRouter
from api.views import TaskViewSet, UserViewSet
router = DefaultRouter()
router.register(r"tasks", TaskViewSet)
router.register(r"users", UserViewSet)

app_name = 'api'
urlpatterns = [

]

urlpatterns.extend(router.urls)