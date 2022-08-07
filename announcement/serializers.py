from rest_framework import serializers
from announcement.models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = [
            'pk',
            # 'writer',
            'title',
            'description',
            'created_time',
            'last_modified',
            'is_important',
            'is_visible',
        ]
