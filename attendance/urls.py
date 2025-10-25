from attendance import views
from django.contrib import admin
from django.urls import path, include

urlpatterns =[
    path('', views.indexPage, name="index"),

    path('admin-home/', views.adminHomePage, name="admin-home"),

    path('admin-attendance/', views.adminAttendancePage, name="admin-attendance"),

    path('admin-department/', views.adminDepartmentPage, name="admin-department"),
    path('add-department/', views.addDepartment, name="add-department"),
    path('admin-edit-department/<int:id>/', views.adminEditDepartment, name="admin-edit-department"),
    path('admin-update-department/<int:id>/', views.adminUpdateDepartment, name="admin-update-department"),
    path('admin-delete-department/<int:id>/', views.adminDeleteDepartment, name="admin-delete-department"),

    path('admin-course/', views.adminCoursePage, name="admin-course"),
    path('add-course/', views.addCourse, name="add-course"),
    path('admin-edit-course/<int:id>/', views.adminEditCourse, name="admin-edit-course"),
    path('admin-update-course/<int:id>/', views.adminUpdateCourse, name="admin-update-course"),
    path('admin-delete-course/<int:id>/', views.adminDeleteCourse, name="admin-delete-course"),

    path('admin-faculty/', views.adminFacultyPage, name="admin-faculty"),
    path('add-faculty/', views.addFaculty, name="add-faculty"),
    path('admin-view-faculty/<int:id>/', views.adminViewFaculty, name="admin-view-faculty"),
    path('admin-edit-faculty/<int:id>/', views.adminEditFaculty, name="admin-edit-faculty"),
    path('admin-update-faculty/<int:id>/', views.adminUpdateFaculty, name="admin-update-faculty"),
    path('admin-delete-faculty/<int:id>/', views.adminDeleteFaculty, name="admin-delete-faculty"),

    path('admin-subject/', views.adminSubjectPage, name="admin-subject"),
    path('add-subject/', views.addSubject, name="add-subject"),
    path('admin-view-subject/<int:id>/', views.adminViewSubject, name="admin-view-subject"),
    path('admin-edit-subject/<int:id>/', views.adminEditSubject, name="admin-edit-subject"),
    path('admin-update-subject/<int:id>/', views.adminUpdateSubject, name="admin-update-subject"),
    path('admin-delete-subject/<int:id>/', views.adminDeleteSubject, name="admin-delete-subject"),

    path('admin-student/', views.adminStudentPage, name="admin-student"),
    path('add-student/', views.addStudent, name="add-student"),
    path('admin-view-student/<int:id>/', views.adminViewStudent, name="admin-view-student"),
    path('admin-edit-student/<int:id>/', views.adminEditStudent, name="admin-edit-student"),
    path('admin-update-student/<int:id>/', views.adminUpdateStudent, name="admin-update-student"),
    path('admin-delete-student/<int:id>/', views.adminDeleteStudent, name="admin-delete-student"),

    path('admin-attendance-details/<int:id>/', views.adminAttendanceDetailsPage, name="admin-attendance-details"),

    path('faculty-home/', views.facultyHomePage, name="faculty-home"),

    path('faculty-attendance/', views.facultyAttendancePage, name="faculty-attendance"),

    path('faculty-student/', views.facultyStudentPage, name="faculty-student"),
    path('faculty-view-student/<int:id>/', views.facultyViewStudent, name="faculty-view-student"),

    path('faculty-attendance-details/<int:id>/', views.facultyAttendanceDetailsPage, name="faculty-attendance-details"),
    path('faculty-take-attendance/', views.facultyTakeAttendancePage, name="faculty-take-attendance"),
    path('save-attendance/', views.saveAttendance, name="save-attendance"),

    path('logout/', views.logout, name="logout"),

    path('get-course/', views.get_course, name="get-course"),
    path('get-subject/', views.get_subject, name="get-subject")
]