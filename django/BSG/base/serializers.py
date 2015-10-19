from rest_framework import serializers
from .models import BusinessProject, User


class BusinessProjectSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')

    class Meta:
        model = BusinessProject
        fields = ('user','key_partners', 'key_values')
