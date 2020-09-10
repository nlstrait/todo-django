from rest_framework import routers
from .api import TodoItemViewSet

router = routers.DefaultRouter()
router.register('api/items', TodoItemViewSet, 'items')

urlpatterns = router.urls