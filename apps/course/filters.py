import django_filters

from apps.course.models import Course


class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = {
            'category__name',
            'category__is_optional',
        }
