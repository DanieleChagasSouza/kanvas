from django.urls import path
from . import views


urlpatterns = [
    path("courses/", views.CourseView.as_view()),
    path("courses/<uuid:pk>/", views.CourseDetailView.as_view()),
    path("courses/<uuid:pk>/contents/", views.CourseContentsCreateView.as_view()),
    path(
        "courses/<uuid:course_pk>/contents/<uuid:content_pk>/",
        views.CourseContentsRetrieve.as_view(),
    ),
    path("courses/<uuid:course_pk>/students/", views.CourseStudentsAdd.as_view()),
    path(
        "courses/<uuid:course_pk>/students/<uuid:student_pk>/",
        views.CourseStudentRemove.as_view(),
    ),
]
