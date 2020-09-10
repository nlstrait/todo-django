from rest_framework import routers
from .api import TodoListViewSet

router = routers.DefaultRouter()
router.register('api/lists', TodoListViewSet, 'lists')

urlpatterns = router.urls