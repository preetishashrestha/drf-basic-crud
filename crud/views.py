from rest_framework import viewsets
from .models import Contact
from .serailizers import ContactSerailizer

class crudView(viewsets.ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class=ContactSerailizer
