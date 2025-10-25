from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from attendance.models import *

# Create your views here.

def indexPage(request):

    if request.method == "POST":
        rol = request.POST.get('rol')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if rol == "admin":
            admin = administrator.get_administrator_by_email_password(email, password)
            if admin:
                request.session['adminId'] = admin.id
                request.session['adminName'] = admin.name
                request.session['adminGmailId'] = admin.gmailId
                request.session['adminMobileNo'] = admin.mobileNo

                return redirect("admin-home")
            else:
                messages.error(request, "Gmail Id or Password are incorrect!")
                return render(request,"index.html")
        else:
            faculties = faculty.get_faculty_by_email_password(email, password)
            if faculties:
                request.session['facultyId'] = faculties.id
                request.session['facultyName'] = faculties.name
                request.session['facultyDesignation'] = faculties.designation
                request.session['facultyGmailId'] = faculties.gmailId
                request.session['facultyMobileNo'] = faculties.mobileNo

                return redirect("faculty-home")
            else:
                messages.error(request, "Gmail Id or Password are incorrect!")
                return render(request,"index.html")
    else:
        return render(request,"index.html")


def adminHomePage(request):

    if request.session.get('adminId'): 

        departmentList = department.objects.all().count()
        courseList = course.objects.all().count()
        facultyList = faculty.objects.all().count()
        classList = attendanceDetails.objects.all().count()
        studentList = student.objects.all().count()

        adminId = request.session.get('adminId')
        adminName = request.session.get('adminName')
        adminGmailId = request.session.get('adminGmailId')
        adminMobileNo = request.session.get('adminMobileNo')

        context = {
            'departmentList' : departmentList,
            'courseList' : courseList,
            'facultyList' : facultyList,
            'classList' : classList,
            'studentList' : studentList,
            'adminId' : adminId,
            'adminName' : adminName,
            'adminGmailId' : adminGmailId,
            'adminMobileNo' : adminMobileNo
        }

        return render(request,"admin-home.html", context)
    
    else:
        return redirect("index")


def adminAttendancePage(request):

    if request.session.get('adminId'):

        adminId = request.session.get('adminId')
        adminName = request.session.get('adminName')
        adminGmailId = request.session.get('adminGmailId')
        adminMobileNo = request.session.get('adminMobileNo')

        departmentList = department.objects.all()
        semesterList = semester.objects.all()
        attendanceList = attendanceDetails.objects.all()

        if request.method == "POST":
            courseId = request.POST['course']
            semesterId = request.POST['semester']
            subjectId = request.POST['subject']

            attendanceList = attendanceDetails.get_attendance_list_by_course_semester_subject(courseId, semesterId, subjectId)

        context = {
            'adminId' : adminId,
            'adminName' : adminName,
            'adminGmailId' : adminGmailId,
            'adminMobileNo' : adminMobileNo,
            'departmentList' : departmentList,
            'semesterList' : semesterList,
            'attendanceList' : attendanceList
        }
        return render(request,"admin-attendance.html", context)

    else:
        return redirect("index")


def adminAttendanceDetailsPage(request, id):

    if request.session.get('adminId'):
        
        studentList = attendance.get_student_by_attendance_id(id)
        attendanceList = attendanceDetails.get_attendance_list_by_id(id)

        studentListAllCount = attendance.get_all_student_by_attendance_id(id)
        studentListPresentCount = attendance.get_present_student_by_action(id)
        studentListAbsentCount = studentListAllCount - studentListPresentCount

        context = {
            'studentList' : studentList,
            'attendanceList' : attendanceList,
            'studentListAllCount' : studentListAllCount,
            'studentListPresentCount' : studentListPresentCount,
            'studentListAbsentCount' : studentListAbsentCount
        }

        return render(request,"admin-attendance-details.html", context)
    else:
        return redirect("index")


def adminDepartmentPage(request):

    if request.session.get('adminId'):

        adminId = request.session.get('adminId')
        adminName = request.session.get('adminName')
        adminGmailId = request.session.get('adminGmailId')
        adminMobileNo = request.session.get('adminMobileNo')

        departmentList = department.objects.all()

        context = {
            'departmentList' : departmentList,
            'adminId' : adminId,
            'adminName' : adminName,
            'adminGmailId' : adminGmailId,
            'adminMobileNo' : adminMobileNo
        }
        
        return render(request,"admin-department.html", context)

    else:
        return  redirect("index")


def addDepartment(request):

    if request.session.get('adminId'):

        if request.method == "POST":
            departmentName = request.POST['department']
            description = request.POST['description']

            data = department(departmentName=departmentName, description=description)
            data.save()

            messages.success(request, "Department added successfully.")

            return redirect("admin-department")
        
    else:
        return redirect("index")


def adminEditDepartment(request, id):

    if request.session.get('adminId'):
        
        departmentList = department.get_department_by_id(id)

        context = {
            'departmentList' : departmentList
        }

        return render(request, "admin-edit-department.html", context)
    else:
        return redirect("index")


def adminUpdateDepartment(request, id):

    if request.session.get('adminId'):

        if request.method == "POST":

            departmentList = department.get_department_by_id(id)
            departmentList.departmentName = request.POST['department']
            departmentList.description = request.POST['description']

            departmentList.save()

            messages.success(request, "Department updated successfully.")

            return redirect("admin-department")
    else:
        return redirect("index")


def adminDeleteDepartment(request, id):

    if request.session.get('adminId'):

        data = department.get_department_by_id(id)
        data.delete()
        messages.error(request, "Department deleted successfully.")
        return redirect("admin-department")
    else:
        return redirect("index")


def adminCoursePage(request):

    if request.session.get('adminId'):

        adminId = request.session.get('adminId')
        adminName = request.session.get('adminName')
        adminGmailId = request.session.get('adminGmailId')
        adminMobileNo = request.session.get('adminMobileNo')

        departmentList = department.objects.all()
        courseList = course.objects.all()

        if request.method == "POST":
            departmentId = request.POST['department']
            courseList = course.get_course_by_department_id(departmentId)

        context = {
            'departmentList' : departmentList,
            'courseList' : courseList,
            'adminId' : adminId,
            'adminName' : adminName,
            'adminGmailId' : adminGmailId,
            'adminMobileNo' : adminMobileNo
        }
        return render(request,"admin-course.html", context)

    else:
        return redirect("index")


def addCourse(request):

    if request.session.get('adminId'):

        if request.method == "POST":
            departmentId = request.POST['department']
            courseName = request.POST['course']
            description = request.POST['description']

            dId = department.get_department_by_id(departmentId)

            data = course(courseName=courseName, description=description, departmentId=dId)
            data.save()

            messages.success(request, "Course added successfully.")
        
            return redirect("admin-course")

    else:
        return redirect("index")


def adminEditCourse(request, id):
    
    if request.session.get('adminId'):
        
        courseList = course.get_course_by_id(id)

        context = {
            'courseList' : courseList
        }

        return render(request, "admin-edit-course.html", context)
    else:
        return redirect("index")


def adminUpdateCourse(request, id):

    if request.session.get('adminId'):
        
        if request.method == "POST":

            courseList = course.get_course_by_id(id)
            courseList.courseName = request.POST['course']
            courseList.description = request.POST['description']

            courseList.save()

            messages.success(request, "Course updated successfully.")
        
            return redirect("admin-course")
    else:
        return redirect("index")


def adminDeleteCourse(request, id):
    
    if request.session.get('adminId'):
        
        data = course.get_course_by_id(id)
        data.delete()
        messages.error(request, "Course deleted successfully.")
        return redirect("admin-course")
    else:
        return redirect("index")


def adminFacultyPage(request):

    if request.session.get('adminId'):

        adminId = request.session.get('adminId')
        adminName = request.session.get('adminName')
        adminGmailId = request.session.get('adminGmailId')
        adminMobileNo = request.session.get('adminMobileNo')

        departmentList = department.objects.all()
        facultyList = faculty.objects.all()

        if request.method == "POST":
            departmentId = request.POST['department']
            facultyList = faculty.get_faculty_by_department_id(departmentId)

        context = {
            'departmentList' : departmentList,
            'facultyList' : facultyList,
            'adminId' : adminId,
            'adminName' : adminName,
            'adminGmailId' : adminGmailId,
            'adminMobileNo' : adminMobileNo
        }
        return render(request,"admin-faculty.html", context)

    else:
        return redirect("index")


def addFaculty(request):

    if request.session.get('adminId'):

        if request.method == "POST":
            departmentId = request.POST['department']
            name = request.POST['name']
            email = request.POST['email']
            number = request.POST['number']
            designation = request.POST['designation']

            dId = department.get_department_by_id(departmentId)

            data = faculty(name=name, designation=designation, gmailId=email, mobileNo=number, departmentId=dId)

            data.save()
            messages.success(request, "Faculty added successfully.")
        
            return redirect('admin-faculty')

    else:
        return redirect("index")


def adminViewFaculty(request, id):

    if request.session.get('adminId'):

        facultyList = faculty.get_faculty_by_id(id)

        context = {
            'facultyList' : facultyList
        }

        return render(request,"admin-view-faculty.html", context)
    else:
        return redirect("index")


def adminEditFaculty(request, id):

    if request.session.get('adminId'):

        facultyList = faculty.get_faculty_by_id(id)

        context = {
            'facultyList' : facultyList
        }

        return render(request, "admin-edit-faculty.html", context)
    else:
        return redirect("index")


def adminUpdateFaculty(request, id):

    if request.session.get('adminId'):

        if request.method == "POST":

            facultyList = faculty.get_faculty_by_id(id)
            facultyList.name = request.POST['name']
            facultyList.gmailId = request.POST['email']
            facultyList.mobileNo = request.POST['number']
            facultyList.designation = request.POST['designation']

            facultyList.save()

            messages.success(request, "Faculty updated successfully.")

            return redirect("admin-faculty")
    else:
        return redirect("index")


def adminDeleteFaculty(request, id):

    if request.session.get('adminId'):

        data = faculty.get_faculty_by_id(id)
        data.delete()
        messages.error(request, "Faculty deleted successfully.")
        return redirect("admin-faculty")
    else:
        return redirect("index")


def adminSubjectPage(request):

    if request.session.get('adminId'):

        adminId = request.session.get('adminId')
        adminName = request.session.get('adminName')
        adminGmailId = request.session.get('adminGmailId')
        adminMobileNo = request.session.get('adminMobileNo')

        departmentList = department.objects.all()
        courseList = course.objects.all()
        semesterList = semester.objects.all()
        subjectList = subject.objects.all()

        if request.method == "POST":
            courseId = request.POST['course']
            semesterId = request.POST['semester']
            subjectList = subject.get_subject_by_course_id_semester_id(courseId, semesterId)

        context = {
            'departmentList' : departmentList,
            'courseList' : courseList,
            'semesterList' : semesterList,
            'subjectList' : subjectList,
            'adminId' : adminId,
            'adminName' : adminName,
            'adminGmailId' : adminGmailId,
            'adminMobileNo' : adminMobileNo
        }

        return render(request,"admin-subject.html", context)

    else:
        return redirect("index")


def addSubject(request):

    if request.session.get('adminId'):

        if request.method == 'POST':
            departmentId = request.POST['department']
            courseId = request.POST['course']
            semesterId = request.POST['semester']
            subjectName = request.POST['subject']

            dId = department.get_department_by_id(departmentId)
            cId = course.get_course_by_id(courseId)
            sId = semester.get_semester_by_id(semesterId)

            data = subject(subjectName=subjectName, courseId=cId, semesterId=sId, departmentId=dId)
            data.save()

            messages.success(request, "Subject added successfully.")

            return redirect('admin-subject')

    else:
        return redirect("index")


def adminViewSubject(request, id):

    if request.session.get('adminId'):
        
        subjectList = subject.get_subject_by_id(id)

        context = {
            'subjectList' : subjectList
        }

        return render(request,"admin-view-subject.html", context)
    else:
        return redirect("index")


def adminEditSubject(request, id):

    if request.session.get('adminId'):
        
        subjectList = subject.get_subject_by_id(id)

        context = {
            'subjectList' : subjectList
        }

        return render(request, "admin-edit-subject.html", context)
    else:
        return redirect("index")


def adminUpdateSubject(request, id):

    if request.session.get('adminId'):
        
        if request.method == 'POST':
            
            subjectList = subject.get_subject_by_id(id)
            subjectList.subjectName = request.POST['subject']

            subjectList.save()

            messages.success(request, "Subject updated successfully.")

            return redirect('admin-subject')
    else:
        return redirect("index")


def adminDeleteSubject(request, id):

    if request.session.get('adminId'):
        
        data = subject.get_subject_by_id(id)
        data.delete()
        messages.error(request, "Subject deleted successfully.")
        return redirect("admin-subject")
    else:
        return redirect("index")


def adminStudentPage(request):

    if request.session.get('adminId'):

        adminId = request.session.get('adminId')
        adminName = request.session.get('adminName')
        adminGmailId = request.session.get('adminGmailId')
        adminMobileNo = request.session.get('adminMobileNo')

        departmentList = department.objects.all()
        courseList = course.objects.all()
        semesterList = semester.objects.all()
        studentList = student.objects.all()

        if request.method == "POST":
            courseId = request.POST['course']
            semesterId = request.POST['semester']
            studentList = student.get_student_by_course_id_semester_id(courseId, semesterId)

        context = {
            'departmentList' : departmentList,
            'courseList' : courseList,
            'semesterList' : semesterList,
            'studentList' : studentList,
            'adminId' : adminId,
            'adminName' : adminName,
            'adminGmailId' : adminGmailId,
            'adminMobileNo' : adminMobileNo
        }

        return render(request,"admin-student.html", context)

    else:
        return redirect("index")


def addStudent(request):

    if request.session.get('adminId'):
    
        if request.method == 'POST':
            departmentId = request.POST['department']
            courseId = request.POST['course']
            semesterId = request.POST['semester']
            studentName = request.POST['name']

            dId = department.get_department_by_id(departmentId)
            cId = course.get_course_by_id(courseId)
            sId = semester.get_semester_by_id(semesterId)

            data = student(studentName=studentName, courseId=cId, semesterId=sId, departmentId=dId)
            data.save()

            messages.success(request, "Student added successfully.")

            return redirect('admin-student')

    else:
        return redirect("index")


def adminViewStudent(request, id):

    if request.session.get('adminId'):
        
        studentList = student.get_student_by_id(id)

        studentTotalAttendaceCount = attendance.get_total_attendance_count_by_studnet(studentList)
        studentPresentAttendaceCount = attendance.get_present_attendance_count_by_studnet(studentList)

        studentAttendancePercentage = int(studentPresentAttendaceCount/studentTotalAttendaceCount*100)

        context = {
            'studentList' : studentList,
            'studentAttendancePercentage' : studentAttendancePercentage
        }

        return render(request,"admin-view-student.html", context)
    else:
        return redirect("index")


def adminEditStudent(request, id):

    if request.session.get('adminId'):
        
        studentList = student.get_student_by_id(id)

        context = {
            'studentList' : studentList
        }

        return render(request,"admin-edit-student.html", context)
    else:
        return redirect("index")


def adminUpdateStudent(request, id):

    if request.session.get('adminId'):
        
        if request.method == 'POST':
            
            studentList = student.get_student_by_id(id)
            studentList.studentName = request.POST['name']

            studentList.save()

            messages.success(request, "Student updated successfully.")

            return redirect('admin-student')
    else:
        return redirect("index")


def adminDeleteStudent(request, id):

    if request.session.get('adminId'):
        
        data = student.get_student_by_id(id)
        data.delete()
        messages.error(request, "Student deleted successfully.")
        return redirect("admin-student")
    else:
        return redirect("index")


def facultyHomePage(request):

    if request.session.get('facultyId'):

        facultyId = request.session.get('facultyId')
        facultyName = request.session.get('facultyName')
        facultyDesignation = request.session.get('facultyDesignation')
        facultyGmailId = request.session.get('facultyGmailId')
        facultyMobileNo = request.session.get('facultyMobileNo')
        dId = faculty.get_department_by_facultyId(facultyId)

        classList = attendanceDetails.get_class_count_by_faculty_id(facultyId)
        studentList = student.get_student_count_by_department_id(dId.departmentId)

        context = {
            'classList' : classList,
            'studentList' : studentList,
            'facultyId' : facultyId,
            'facultyName' : facultyName,
            'facultyDesignation' : facultyDesignation,
            'facultyGmailId' : facultyGmailId,
            'facultyMobileNo' : facultyMobileNo,
            'dId' : dId
        }
        return render(request,"faculty-home.html", context)
    
    else:
        return redirect("index")


def facultyAttendancePage(request):

    if request.session.get('facultyId'):

        facultyId = request.session.get('facultyId')
        facultyName = request.session.get('facultyName')
        facultyDesignation = request.session.get('facultyDesignation')
        facultyGmailId = request.session.get('facultyGmailId')
        facultyMobileNo = request.session.get('facultyMobileNo')
        dId = faculty.get_department_by_facultyId(facultyId)

        courseList = course.get_course_by_department_id(dId.departmentId)
        semesterList = semester.objects.all()
        attendanceList = attendanceDetails.get_attendance_list_by_faculty_id(facultyId)
        
        if request.method == "POST":
            courseId = request.POST['course']
            semesterId = request.POST['semester']
            subjectId = request.POST['subject']

            attendanceList = attendanceDetails.get_attendance_list_by_faculty_course_semester_subject(facultyId, courseId, semesterId, subjectId)

        context = {
            'courseList' : courseList,
            'semesterList' : semesterList,
            'attendanceList' : attendanceList,
            'facultyId' : facultyId,
            'facultyName' : facultyName,
            'facultyDesignation' : facultyDesignation,
            'facultyGmailId' : facultyGmailId,
            'facultyMobileNo' : facultyMobileNo,
            'dId' : dId
        }

        return render(request,"faculty-attendance.html", context)

    else:
        return redirect("index")


def facultyAttendanceDetailsPage(request, id):

    if request.session.get('facultyId'):
        
        studentList = attendance.get_student_by_attendance_id(id)
        attendanceList = attendanceDetails.get_attendance_list_by_id(id)

        studentListAllCount = attendance.get_all_student_by_attendance_id(id)
        studentListPresentCount = attendance.get_present_student_by_action(id)
        studentListAbsentCount = studentListAllCount - studentListPresentCount

        context = {
            'studentList' : studentList,
            'attendanceList' : attendanceList,
            'studentListAllCount' : studentListAllCount,
            'studentListPresentCount' : studentListPresentCount,
            'studentListAbsentCount' : studentListAbsentCount
        }

        return render(request,"faculty-attendance-details.html", context)
    else:
        return redirect("index")


def facultyTakeAttendancePage(request):

    if request.session.get('facultyId'):

        if request.method == "POST":
            departmentId = request.POST['department']
            courseId = request.POST['course']
            semesterId = request.POST['semester']
            subjectId = request.POST['subject']
            date = request.POST['date']

            studentList = student.get_student_by_course_id_semester_id(courseId, semesterId)
            courseList = course.get_course_by_id(courseId)
            semesterList = semester.get_semester_by_id(semesterId)
            subjectList = subject.get_subject_by_id(subjectId)

            context = {
                'courseId' : courseId,
                'semesterId' : semesterId,
                'subjectId' : subjectId,
                'courseList' : courseList,
                'semesterList' : semesterList,
                'subjectList' : subjectList,
                'date' : date,
                'studentList' : studentList
            }

            return render(request,"faculty-take-attendance.html", context)

    else:
        return redirect("index")
    


def saveAttendance(request):

    actionList = []
    studentList = []

    facultyId = request.session.get('facultyId')
    facultyList = faculty.get_faculty_by_id(facultyId)
    dId = faculty.get_department_by_facultyId(facultyId)

    if request.method == "POST":
        courseId = request.POST['course']
        semesterId = request.POST['semester']
        subjectId = request.POST['subject']
        date = request.POST['date']
        action_id = request.POST.getlist('action')

        crsId = course.get_course_by_id(courseId)
        smstrId = semester.get_semester_by_id(semesterId)
        sbjctId = subject.get_subject_by_id(subjectId)

        data = attendanceDetails(courseId=crsId, semesterId=smstrId, subjectId=sbjctId, facultyId=facultyList, date= date)
        data.save()

        last_data = attendanceDetails.objects.last()

        for x in action_id:
            actionList.append(x[0])
            studentList.append(x[2])

        for id, action in zip(studentList, actionList):
            studentId = id
            actiondata = action
            stdId = student.get_student_by_id(studentId)

            data1 = attendance(studentRollNo=stdId, action=actiondata, attendanceDetailsId=last_data)
            data1.save()

        return redirect("faculty-attendance")


def facultyStudentPage(request):

    if request.session.get('facultyId'):

        facultyId = request.session.get('facultyId')
        facultyName = request.session.get('facultyName')
        facultyDesignation = request.session.get('facultyDesignation')
        facultyGmailId = request.session.get('facultyGmailId')
        facultyMobileNo = request.session.get('facultyMobileNo')
        dId = faculty.get_department_by_facultyId(facultyId)

        courseList = course.get_course_by_department_id(dId.departmentId)
        semesterList = semester.objects.all()
        studentList = student.get_student_by_department_id(dId.departmentId)

        if request.method == "POST":
            courseId = request.POST['course']
            semesterId = request.POST['semester']
            studentList = student.get_student_by_course_id_semester_id(courseId, semesterId)

        context = {
            'courseList' : courseList,
            'semesterList' : semesterList,
            'studentList' : studentList,
            'facultyId' : facultyId,
            'facultyName' : facultyName,
            'facultyDesignation' : facultyDesignation,
            'facultyGmailId' : facultyGmailId,
            'facultyMobileNo' : facultyMobileNo,
            'dId' : dId
        }
        return render(request,"faculty-student.html", context)

    else:
        return redirect("index")


def facultyViewStudent(request, id):

    if request.session.get('facultyId'):

        TotalAttendaceCount = 0
        PresentAttendaceCount = 0

        facultyId = request.session.get('facultyId')        
        studentList = student.get_student_by_id(id)

        attendanceListData = attendanceDetails.get_attendance_list_by_faculty_id(facultyId)

        for attendanceList in attendanceListData:

            studentTotalAttendaceCount = attendance.get_total_attendance_count_by_studnet_attendanceList(studentList, attendanceList)

            TotalAttendaceCount += studentTotalAttendaceCount

            studentPresentAttendaceCount = attendance.get_present_attendance_count_by_studnet_attendanceList(studentList, attendanceList)

            PresentAttendaceCount += studentPresentAttendaceCount

        if TotalAttendaceCount:
            studentAttendancePercentage = int(PresentAttendaceCount/TotalAttendaceCount*100)
        else:
            studentAttendancePercentage = 0

        context = {
            'studentList' : studentList,
            'studentAttendancePercentage' : studentAttendancePercentage
        }

        return render(request,"faculty-view-student.html", context)
    else:
        return redirect("index")


def logout(request):
    request.session.clear()
    return redirect('index')


def get_course(request):
    department_id = request.GET['department_id']
    courseList = course.get_course_by_department_id(department_id)
    return render(request, 'get-course.html', locals())


def get_subject(request):
    course_id = request.GET['course_id']
    semester_id = request.GET['semester_id']
    subjectList = subject.get_subject_by_course_id_semester_id(course_id, semester_id)
    return render(request, 'get-subject.html', locals())