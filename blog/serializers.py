from rest_framework import serializers

from about.serializers import LocationSerializer, SocialNetworkSerializer, TestimonialsSerializer, ClientsSerializer
from blog.models import User, CurrentProgress, Blog
from blog.models.goals import Goal


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'image', 'created_at')


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('title', 'description', 'icon')


class CurrentProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentProgress
        fields = ('name', 'description', 'icon')


class UserAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('about',)


class UserContactSerializer(serializers.ModelSerializer):
    # social_network = SocialNetworkSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'full_name', 'phone',
                  'birth_date', 'email',
                  'location', 'image', 'job_name')

# https://stackoverflow.com/questions/45275897/how-to-get-superuser-details-in-django
