from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from blog.models import User, get_my_model_super_user
from blog.serializers import BlogSerializer


class SupperUserBlogAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):

        user = get_my_model_super_user()
        blog_queryset = user.blogs.all()
        blog_serializer = BlogSerializer(blog_queryset, many=True)
        return Response(data=blog_serializer.data)
        # pass


class BlogAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk):
        if not User.objects.filter(user_name=pk).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        user = User.objects.get(user_name=pk)
        blog_queryset = user.blogs.all()
        blog_serializer = BlogSerializer(blog_queryset, many=True)
        return Response(data=blog_serializer.data)
