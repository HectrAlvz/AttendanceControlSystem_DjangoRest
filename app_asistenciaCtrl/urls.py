from rest_framework import routers
from .api import CompanyViewSet, WorkerViewSet, AttendanceViewSet
router = routers.DefaultRouter()

router.register('api/company', CompanyViewSet, 'company')
router.register('api/worker', WorkerViewSet, 'worker')
router.register('api/attendance', AttendanceViewSet, 'attendance')

urlpatterns = router.urls