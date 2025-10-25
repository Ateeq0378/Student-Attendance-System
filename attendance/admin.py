from django.contrib import admin
from attendance.models import *
# Register your models here.

class forAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gmailId', 'mobileNo']


class forDepartment(admin.ModelAdmin):
    list_display = ['id', 'departmentName', 'description']


class forFaculty(admin.ModelAdmin):
    list_display = ['id', 'name', 'designation', 'mobileNo', 'gmailId', 'departmentId']


class forCourse(admin.ModelAdmin):
    list_display = ['id', 'courseName', 'description', 'departmentId']


class forSemester(admin.ModelAdmin):
    list_display = ['id', 'semester']


class forStudent(admin.ModelAdmin):
    list_display = ['id', 'studentName', 'courseId', 'semesterId', 'departmentId']


class forSubject(admin.ModelAdmin):
    list_display = ['id', 'subjectName', 'courseId', 'semesterId', 'departmentId']


class forAttendanceDetails(admin.ModelAdmin):
    list_display = ['id', 'courseId', 'semesterId', 'subjectId', 'facultyId', 'date']


class forAttendance(admin.ModelAdmin):
    list_display = ['id', 'studentRollNo', 'action', 'attendanceDetailsId']


admin.site.register(administrator, forAdmin)
admin.site.register(department, forDepartment)
admin.site.register(faculty, forFaculty)
admin.site.register(course, forCourse)
admin.site.register(semester, forSemester)
admin.site.register(student, forStudent)
admin.site.register(subject, forSubject)
admin.site.register(attendanceDetails, forAttendanceDetails)
admin.site.register(attendance, forAttendance)