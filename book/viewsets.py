from rest_framework import viewsets
from .models import Book
from .serializer import BookSerialier

class BookViewSet(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerialier