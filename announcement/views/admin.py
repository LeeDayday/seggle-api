from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Announcement
from ..serializers import AnnouncementSerializer
from django.http import Http404
from rest_framework.generics import get_object_or_404
# Create your views here.

class ListAnnouncementsAdmin(APIView):
    """
    Admin 공지 사항 리스트
    """
    # 04-01 공지 리스트 전체 조회
    def get(self, request):
        announcements = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 00-12 공지 생성
    def post(self, request):
        data = request.data
        announcement = {
            "title": data["title"],
            "description": data["description"],
            "visible": data["is_visible"],
            "important": data["is_important"],
            # writer
        }
        serializer = AnnouncementSerializer(data=announcement)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListAnnouncementsDetailAdmin(APIView):
    """
    공지 사항 세부 사항
    """
    # 해당 pk에 해당하는 공지사항 object 불러오기
    def get_object(self, pk):
        try:
            return Announcement.objects.get(pk=pk)
        except Announcement.DoesNotExist:
            raise Http404

    # 00-13 공지 사항 수정
    def put(self, request, pk):
        announcement = self.get_object(pk)
        serializer = AnnouncementSerializer(announcement)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 00-14 공지 사항 삭제
    def delete(self, request, pk):
        announcement = self.get_object(pk)
        announcement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 00-16 공지 사항 조회
    def get(self, request, pk):
        announcement = self.get_object(pk)
        serializer = AnnouncementSerializer(announcement)
        return Response(serializer.data)

class ListAnnouncementCheckAdmin(APIView):
    """
    공지사항 important, visible
    """
    # 00-15 공지 사항 important, visible 수정
    def put(self, request, pk):
        announcement = get_object_or_404(Announcement, pk=pk)
        data = request.data
        obj = {
            "important": data["is_important"],
            "visible": data["is_visible"]
        }
        serializer = AnnouncementSerializer(announcement, data=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)