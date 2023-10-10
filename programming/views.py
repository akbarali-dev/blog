from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from django.contrib.auth.models import User as SuperUser
from rest_framework.response import Response
from rest_framework import generics

from about.models import Education
from blog.models import User, get_my_model_super_user
from programming.models import Experience, Skills
from programming.serializers import *


def get_resume_data(user: User) -> Response:
    education_queryset = user.education.all()
    experience_queryset = user.experience.all()
    technology_queryset = user.technologies.all()
    education_serializer = EducationSerializer(education_queryset, many=True)
    experience_serializer = ExperienceSerializer(experience_queryset, many=True)
    technology_serializer = SkillsSerializer(technology_queryset, many=True)

    return Response({
        "education": education_serializer.data,
        "experience": experience_serializer.data,
        "skill": technology_serializer.data
    })


def get_portfolio_data(user: User) -> Response:
    portfolio_queryset = user.portfolio.all()
    portfolio_serializer = PortfolioSerializer(portfolio_queryset, many=True)
    category_set = set()
    for portfolio in portfolio_queryset:
        for category in portfolio.category.all():
            category_set.add(category)
    category_serializer = CategorySerializer(category_set, many=True)
    return Response({
        "portfolio": portfolio_serializer.data,
        "category": category_serializer.data
    })


class PortfolioApiView(APIView):
    def get(self, request, pk):
        if not User.objects.filter(user_name=pk).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        user = User.objects.get(user_name=pk)
        return get_portfolio_data(user)


class SuperUserPortfolioAPIView(APIView):
    def get(self, request):
        user = get_my_model_super_user()

        return get_portfolio_data(user)


class ResumeApiView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(user_name=pk)
            return get_resume_data(user)
        except User.DoesNotExist:
            return Response(data='User not found', status=status.HTTP_404_NOT_FOUND)


class SuperUserResumeAPIView(APIView):
    def get(self, request):
        super_user = SuperUser.objects.filter(username='akbarali').first()
        user = User.objects.get(auth_user=super_user)
        return get_resume_data(user)
