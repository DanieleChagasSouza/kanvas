from rest_framework import serializers

from accounts.models import Account
from students_courses.models import StudentCourse
from .models import Course
from students_courses.serializers import StudentCourseSerializer
from contents.serializers import ContentSerializer
from rest_framework.validators import UniqueValidator


class CourseSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)
    students_courses = StudentCourseSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]

    name = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=Course.objects.all(),
                message="course with this name already exists.",
            )
        ],
    )


class CourseStudentAddSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True, required=False)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]
        read_only_fields = ["id", "name"]

    def update(self, instance, validated_data):
        list_email = []

        for student_email in validated_data["students_courses"]:
            email = student_email["student"]["email"]
            try:
                student = Account.objects.get(email=email)
                try:
                    StudentCourse.objects.get(student=student, course=instance)
                except:
                    instance.students.add(student)
                    instance.save()
                return instance
            except Account.DoesNotExist:
                list_email.append(email)
            if len(list_email) > 0:
                raise serializers.ValidationError(
                    {
                        "detail": f"No active accounts was found: {', '.join(list_email)}."
                    }
                )
