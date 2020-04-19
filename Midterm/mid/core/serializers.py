from django.shortcuts import render
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated


from core.models import Book, Journal

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'numpages')

    def validate_numpages(self, numpages):
        if numpages < 0:
            raise serializers.ValidationError('Numpages must be greater than 0')
        return numpages

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('id', 'name', 'type')

    def validate_type(self, type):
        if type > 0 or type < 5:
            raise serializers.ValidationError('Type is invalid')
        return type