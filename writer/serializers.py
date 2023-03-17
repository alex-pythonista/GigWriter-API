from rest_framework import serializers


class StringListField(serializers.ListField):
    child = serializers.CharField()


class WriterSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    keywords = StringListField(required=False)
    skills = StringListField(required=False)
    experience = serializers.ChoiceField(
        choices=['beginner', 'intermediate', 'expert'],
        required=False
    )
    service_type = serializers.CharField(required=False)
    target_audience = StringListField(required=False)
    prompt = serializers.CharField(required=False)