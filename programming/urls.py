from django.urls import path

from programming.views import SuperUserResumeAPIView, ResumeApiView, PortfolioApiView, SuperUserPortfolioAPIView

urlpatterns = [
    # path('', include(router.urls)),
    # path('resume/<str:pk>/', UserAboutAPIView.as_view()),

    path('portfolio/<str:pk>/', PortfolioApiView.as_view()),
    path('portfolio/', SuperUserPortfolioAPIView.as_view()),
    path('resume/<str:pk>/', ResumeApiView.as_view()),
    path('resume/', SuperUserResumeAPIView.as_view()),

]
