"""

Serializers : A serializer translates data into a format that is easy to
              consume over the internet, typically JSON, and is displayed
              at an API endpoint.

"""
from rest_framework import serializers

from books.models import Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author', 'isbn')
