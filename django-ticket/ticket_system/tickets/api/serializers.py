from rest_framework.serializers import ModelSerializer
from tickets.models import Ticket


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]
