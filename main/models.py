from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    room = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    lessons = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/teachers/%i/" % self.id


class TeacherImage(models.Model):
    teacher = models.ForeignKey(Teacher)
    image = models.FileField(upload_to='teacher/images')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return str(self.id)
