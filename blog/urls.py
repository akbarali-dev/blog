from django.urls import path

from blog.views import SupperUserBlogAPIView, BlogAPIView

urlpatterns = [
    # path('', include(router.urls)),
    # path('resume/<str:pk>/', UserAboutAPIView.as_view()),

    path('blogs/<str:pk>/', BlogAPIView.as_view()),
    path('blogs/', SupperUserBlogAPIView.as_view()),

]