from rest_framework import routers
from leads.views import LeadViewSet

router = routers.DefaultRouter()
router.register('leads', LeadViewSet, 'leads')

urlpatterns = router.urls
