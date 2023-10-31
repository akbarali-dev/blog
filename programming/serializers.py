from rest_framework import serializers

from about.models import Education
from programming.models import Experience, Skills, Technology, Portfolio, Category


class CategorySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()


class PortfolioSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Portfolio
        fields = ('id','name', 'description', 'category', 'image')


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('name', 'start_year', 'graduation_year', 'description')


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('name', 'start_year', 'graduation_year', 'description')


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ('name', 'discount',)


class TechnologySerializer(serializers.ModelSerializer):
    skills = SkillsSerializer(many=True)

    class Meta:
        model = Technology
        fields = ('name', 'discount', 'skills')
