from rest_framework import serializers


class StringListField(serializers.ListField):
    child = serializers.CharField()


class WriterSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    keywords = StringListField(required=False)
    target_audience = StringListField(required=False)
    portfolio = serializers.URLField(required=False)
    prompt = serializers.CharField(required=False)