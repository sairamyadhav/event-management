from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Event, EventUser
from user.serializers import UserSerializer

class EventUserSerializer(ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = EventUser
        fields = ['user', 'owner']

class EventSerializer(ModelSerializer):

    users = EventUserSerializer(many=True, source="eventuser_set")
    users_count = serializers.IntegerField(source='number_of_users', read_only=True)

    class Meta:
        model = Event
        fields = ['name', 'description', 'users', 'is_private', 'limit', 'event_status', 'starts_at', 'venue', 'users_count']
        read_only_fields = ['users', 'eventuser_set']

    def create(self, validated_data):
        validated_data.pop('eventuser_set')
        event = Event.objects.create(**validated_data)
        return event
