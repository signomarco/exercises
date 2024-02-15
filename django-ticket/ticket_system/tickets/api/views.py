from rest_framework import viewsets
from tickets.models import Ticket
from .serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        if query := self.request.GET.get('q'):
            queryset = queryset.filter(title__icontains=query)
        
        return queryset
