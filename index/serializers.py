from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['firstname', 'lastname', 'email', 'phone', 'letter', 'division', 'portfolio_link', 'status']
