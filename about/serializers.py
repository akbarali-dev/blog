from rest_framework import serializers

from about.models import SocialNetwork, Location, Testimonials, Client, Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('user', 'full_name', 'email', 'description')


class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ('name', 'link', 'icon')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'link',)


class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = ('full_name', 'description', 'image')


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'description', 'image')
