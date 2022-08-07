from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Announcement
from ..serializers import AnnouncementSerializer
from django.http import Http404
from rest_framework.generics import get_object_or_404
# Create your views here.
class ListAnnouncements(APIView):
    """
    공지 사항 리스트
    """
    # 04-01 공지 리스트 전체 조회
    def get(self, request):
        announcements = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data)

class ListAnnouncementsDetail(APIView):
    """
    공지 사항 세부 사항
    """
    # 해당 pk에 해당하는 공지사항 object 불러오기
    def get_object(self, pk):
        try:
            return Announcement.objects.get(pk=pk)
        except Announcement.DoesNotExist:
            raise Http404

    # 00-16 공지 사항 조회
    def get(self, request, pk):
        announcement = self.get_object(pk)
        serializer = AnnouncementSerializer(announcement)
        return Response(serializer.data)
