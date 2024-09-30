from .models import Event
from rest_framework import viewsets
from .serializers import EventSerializer
from rest_framework.response import Response
from django.db.models import Count

# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        query_params = request.query_params
        order_by = query_params.get('sort', None)
        queryset = self.get_queryset()
        if order_by:
            queryset = queryset.annotate(number_of_users=Count('eventuser'))
            sort_order = '' if order_by == 'asc' else '-'
            sort_order += 'number_of_users'
            queryset = queryset.order_by(sort_order)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            event_data = dict(request.data)
            event_data['users'] = []
            serializer = self.get_serializer(data=event_data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            serializer.save()
            return Response(data)
        except Exception as e:
            return Response({'message': str(e)})
