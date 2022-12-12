from rest_framework import serializers

from api.models import StatusCode


class StatusCodeSerializer(serializers.Serializer):
    
    id            = serializers.IntegerField(read_only=True)

    code          = serializers.IntegerField()
    name          = serializers.CharField(max_length=50)
    description   = serializers.CharField(max_length=250)

    # created_at    = serializers.DateTimeField(read_only=True)
    # last_modified = serializers.DateTimeField(read_only=True)




    class Meta:
        model = StatusCode
