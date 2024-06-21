from quickstart.serializers import ListingSerializer
from quickstart.models import Listing
from rest_framework import permissions, viewsets

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
