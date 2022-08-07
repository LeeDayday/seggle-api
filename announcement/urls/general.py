from django.urls import path
from ..views.general import ListAnnouncements, ListAnnouncementsDetail

urlpatterns = [
    path('', ListAnnouncements.as_view()),
    path('<int:pk>', ListAnnouncementsDetail.as_view()),
]
