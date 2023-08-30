from http.client import NOT_FOUND
from django.shortcuts import get_object_or_404
from students_courses.models import StudentCourse
from .models import Course
from accounts.models import Account
from contents.models import Content
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import CourseSerializer, CourseStudentAddSerializer
from contents.serializers import ContentSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from accounts.permissions import CanAccessContent, IsAccountOwner, IsAdminOrReadOnly
from drf_spectacular.utils import extend_schema


class CourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @extend_schema(
        operation_id="course_create",
        summary="create course",
        description="route to create all course",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        operation_id="courses_list",
        summary="list courses",
        description="route to list all courses",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CourseDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @extend_schema(
        operation_id="courses_list",
        summary="list courses",
        description="route to list all courses",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="course_update",
        summary="update course",
        description="route to list all update",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(operation_id="courses_put", exclude=True)
    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(operation_id="courses_delete", exclude=True)
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class CourseContentsCreateView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        course_id = self.kwargs.get("pk")
        course = get_object_or_404(Course, pk=course_id)
        serializer.save(course=course)

    @extend_schema(
        operation_id="CourseContents_create",
        summary="create course contents",
        description="route to create all CourseContents",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CourseContentsRetrieve(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CanAccessContent]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "content_pk"

    @extend_schema(
        operation_id="CourseContents_list",
        summary="list by id course contents",
        description="route to list all CourseContents",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="course_update",
        summary="update by id course contents",
        description="route to update all course contents",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="course_delete",
        summary="delete by id course contents",
        description="route to delete all course contents",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(operation_id="CourseContents_put", exclude=True)
    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class CourseStudentsAdd(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CourseStudentAddSerializer
    queryset = Course.objects.all()

    def get_object(self):
        course_id = self.kwargs["course_pk"]
        course = Course.objects.get(pk=course_id)
        return course

    @extend_schema(
        operation_id="CourseStudents_Add",
        summary="list by id course students",
        description="route to list all CourseContents",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="CourseStudents_put",
        summary="Add student to course",
        description="route add student to course",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class CourseStudentRemove(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly, CanAccessContent]
    queryset = Course.objects.all()
    serializer_class = CourseStudentAddSerializer
    lookup_url_kwarg = "course_pk"

    def perform_destroy(self, instance):
        student = get_object_or_404(Account, pk=self.kwargs["student_pk"])
        course_students = instance.students.all()
        if student not in course_students:
            raise NotFound({"detail": "this id is not associated with this course."})
        else:
            instance.students.remove(student)

    @extend_schema(
        operation_id="courseStudents_delete",
        summary="delete by id course students",
        description="route to delete all course students",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
