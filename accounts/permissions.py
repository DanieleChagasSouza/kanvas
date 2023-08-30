from rest_framework.views import View
from rest_framework import permissions
from .models import Account
from courses.models import Course
from django.shortcuts import get_object_or_404


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or request.user.is_superuser


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Course) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            and request.user in obj.students.all()
            or request.user.is_superuser
        )


class CanAccessContent(permissions.BasePermission):
    def has_permission(self, request, view):
        course_id = view.kwargs.get("course_pk")
        if request.user.is_superuser:
            return True
        course = get_object_or_404(Course, id=course_id)
        list_students = course.students.all()
        if request.user in list_students:
            return True
        return False
