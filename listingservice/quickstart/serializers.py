from rest_framework import serializers
from quickstart.models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'salary', 'hours', 'companyid', 'created']
    