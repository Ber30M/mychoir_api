from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'Chant', views.ChantViewSet)
router.register(r'Choriste', views.ChoristeViewSet)
router.register(r'Attendance', views.AttendanceViewSet)
router.register(r'Event', views.EventViewSet)
router.register(r'Temps_liturgique', views.Temps_liturgiqueViewSet)
router.register(r'Partie_eucharistique', views.Partie_eucharistiqueViewSet)

urlpatterns = [
    path('', include(router.urls)),
#     path('login/', TokenPairView.as_view()),
#     path('refresh/', TokenRefreshView.as_view())
]


