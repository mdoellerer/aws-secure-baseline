from django.contrib import admin
from django.urls import include, path
from rest_framework.views import APIView
from rest_framework.response import Response


class HealthView(APIView):
    def get(self, request):
        return Response({"status": "ok"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/health/", HealthView.as_view(), name="health"),
    path("api/", include("api.urls")),
]
