from django.utils.timezone import now
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from displays.models import SlideShow, Screen


class ScreenContentView(APIView):
    def get(self, request, screen_code):
        screen = Screen.objects.filter(code=screen_code).first()
        if not screen:
            return Response({"error": "Screen not found"}, status=status.HTTP_404_NOT_FOUND)

        content = (
            screen.contents
                    #.filter(time_range__contains=now())
                   .order_by('-priority')
                   .first()
        )

        if not content:
            return Response({"error": "No active content"}, status=status.HTTP_404_NOT_FOUND)

        slides = content.slide_show.slides.all().order_by('order')
        return Response({
            "type": "slides",
            "images": [{
                "url": slide.image.url,
                "duration": slide.duration,
                "order": slide.order
            } for slide in slides]
        })

        return Response({"error": "Unsupported content type"}, status=status.HTTP_400_BAD_REQUEST)
