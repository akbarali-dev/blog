from rest_framework import serializers

from about.models import SocialNetwork, Location, Testimonials, Client, Contact, Icon


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('user', 'full_name', 'email', 'description', )


class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icon
        fields = ('code',)


class SocialNetworkSerializer(serializers.ModelSerializer):
    icon = IconSerializer()

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
        fields = ('full_name', 'description', 'image', 'created_at')


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'description', 'image')
