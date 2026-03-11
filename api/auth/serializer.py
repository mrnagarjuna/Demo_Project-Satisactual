from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        # Custom validation logic can be added here
        return attrs

class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(required=True)

    def validate(self, attrs):
        if not attrs.get('refresh_token'):
            raise serializers.ValidationError("Refresh token is required.")
        return attrs