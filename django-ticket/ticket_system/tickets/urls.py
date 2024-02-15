from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="tickets/index.html")),
    path("api/", include("tickets.api.urls")),
]

# if settings.DEBUG:
#     urlpatterns += 