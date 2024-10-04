from rest_framework import serializers

class TranslationRequestSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=500)

class TranslationResponseSerializer(serializers.Serializer):
    translated_text = serializers.CharField(max_length=500)
