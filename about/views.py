from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import action

from django.contrib.auth.models import User as SuperUser

from about.serializers import LocationSerializer, SocialNetworkSerializer, TestimonialsSerializer, ClientsSerializer, \
    ContactSerializer
from blog.models import User, Visitor
from blog.serializers import UserAboutSerializer, UserContactSerializer, CurrentProgressSerializer, GoalSerializer


# Create your views here.

def get_contact_data(user: User) -> Response:
    location_queryset = user.location
    social_network_queryset = user.social_network.all()

    social_network_serializer = SocialNetworkSerializer(social_network_queryset, many=True)
    contact_serializer = UserContactSerializer(user)
    location_serializer = LocationSerializer(location_queryset)

    return Response({
        "contact": contact_serializer.data,
        'location': location_serializer.data,
        "socialNetwork": social_network_serializer.data
    })


def get_about_data(user: User) -> Response:
    current_progress_queryset = user.current_progress.all()
    goals_queryset = user.goals.all()
    testimonials_queryset = user.testimonials.all()
    clients_queryset = user.clients.all()
    current_progress_serializer = CurrentProgressSerializer(current_progress_queryset, many=True)
    goals_serializer = GoalSerializer(goals_queryset, many=True)
    testimonials_serializer = TestimonialsSerializer(testimonials_queryset, many=True)
    clients_serializer = ClientsSerializer(clients_queryset, many=True)
    about_serializer = UserAboutSerializer(user)
    return Response({
        "currentProgress": current_progress_serializer.data,
        "goals": goals_serializer.data,
        "testimonials": testimonials_serializer.data,
        "clients": clients_serializer.data,
        "about": user.about,
    })


class VisitorStatistics(APIView):
    def get(self, request):
        visitor_count = Visitor.objects.values('ip_address').distinct().count()
        return Response({'visitor_count': visitor_count})


class ContactAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = ContactSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data="Successfully saved")


class UserAboutAPIView(APIView):
    def get(self, request, pk):
        if not User.objects.filter(user_name=pk).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        user = User.objects.get(user_name=pk)
        return get_about_data(user)


class SuperUserAboutAPIView(APIView):
    def get(self, request):
        super_user = SuperUser.objects.filter(username='akbarali').first()
        user = User.objects.get(auth_user=super_user)
        return get_about_data(user)


class SuperUserContactView(APIView):
    def get(self, request):
        super_user = SuperUser.objects.filter(username='akbarali').first()
        user = User.objects.get(auth_user=super_user)

        return get_contact_data(user)


class UserContactView(APIView):
    def get(self, request, pk):
        if not User.objects.filter(user_name=pk).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        return get_contact_data(user=User.objects.get(user_name=pk))


class UserAboutViewSet(ModelViewSet):
    super_user = SuperUser.objects.filter(username='akbarali').first()
    # print(super_user)
    queryset = User.objects.filter(auth_user=super_user)
    serializer_class = UserAboutSerializer

    # @action(methods=['get'], detail=True)
    # def get_queryset(self, **kwargs):
    #     print('request: ', self.request.query_params)
    # username = self.request.data
    # queryset = User.objects.filter(user_name=username)
    # return queryset


class UserContactViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserContactSerializer
