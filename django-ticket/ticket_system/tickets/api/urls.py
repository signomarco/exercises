from rest_framework.routers import DefaultRouter
from .views import TicketViewSet
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r"tickets", TicketViewSet)

urlpatterns = router.urls

urlpatterns += [
    # authentication
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]