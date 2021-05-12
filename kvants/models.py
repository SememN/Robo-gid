from django.db import models


# models with kvants description
class Description(models.Model):
    name = models.CharField(max_length=30)
    preview = models.CharField(max_length=300)
    description = models.TextField(max_length=5000)


class ItDescription(Description):
    pass


class AutoDescription(Description):
    pass


class AeroDescription(Description):
    pass


class MathDescription(Description):
    pass


class PromDesDescription(Description):
    pass


class PromRoboDescription(Description):
    pass


class HiTechDescription(Description):
    pass


class ChessCDescription(Description):
    pass


# models describing kvantorium courses
class Course(models.Model):
    link = models.CharField(max_length=300)
    preview = models.CharField(max_length=300)
    name = models.CharField(max_length=30)
    direction = models.CharField(max_length=10)
    level = models.CharField(max_length=11)
    description = models.CharField(max_length=300)


class ItCourse(Course):
    pass


class AutoCourse(Course):
    pass


class AeroCourse(Course):
    pass


class MathCourse(Course):
    pass


class PromDesCourse(Course):
    pass


class PromRoboCourse(Course):
    pass


class HiTechCourse(Course):
    pass


class ChessCourse(Course):
    pass
