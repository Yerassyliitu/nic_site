from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['firstname', 'lastname', 'email', 'phone', 'letter', 'division', 'portfolio_link', 'university']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if self.context['request'].method == 'GET':
            data['id'] = instance.id
            data['status'] = instance.status
        return data