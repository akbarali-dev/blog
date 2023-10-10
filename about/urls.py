from django.urls import path, include
from rest_framework.routers import DefaultRouter
from about.views import UserAboutViewSet, UserContactViewSet, UserAboutAPIView, SuperUserAboutAPIView, SuperUserContactView, UserContactView, ContactAPIView

# router = DefaultRouter()
# router.register('user-about', UserAboutViewSet)
# router.register('user-contact', UserContactViewSet)
# router.register()
urlpatterns = [
    # path('', include(router.urls)),
    path('user-about/<str:pk>/', UserAboutAPIView.as_view()),
    path('user-about/', SuperUserAboutAPIView.as_view()),
    path('user-contact/', SuperUserContactView.as_view()),
    path('user-contact/<str:pk>', UserContactView.as_view()),
    path('contact-save/', ContactAPIView.as_view()),

]
