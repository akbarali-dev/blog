from rest_framework import serializers

from about.models import Education
from programming.models import Experience, Skills, Technology, Portfolio, Category


class PortfolioSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer(many=True)

    class Meta:
        model = Portfolio
        fields = ('name', 'description', 'category',)


class CategorySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('name', 'start_year', 'graduation_year', 'description')


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('name', 'start_year', 'graduation_year', 'description')


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ('name', 'discount')


class SkillsSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True)

    class Meta:
        model = Skills
        fields = ('name', 'discount',)
