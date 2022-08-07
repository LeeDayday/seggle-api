from django.urls import path
from ..views.admin import ListAnnouncementsAdmin, ListAnnouncementsDetailAdmin, ListAnnouncementCheckAdmin

urlpatterns = [
    path('', ListAnnouncementsAdmin.as_view()),
    path('<int:pk>', ListAnnouncementsDetailAdmin.as_view()),
    path('<int:pk>/check/', ListAnnouncementCheckAdmin.as_view())
]
