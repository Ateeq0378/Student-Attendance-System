from django.db import models

# Create your models here.

class administrator(models.Model):
    name = models.CharField(max_length = 50)
    gmailId = models.CharField(max_length = 50)
    mobileNo = models.CharField(max_length = 10)

    @staticmethod
    def get_administrator_by_email(email):
        try:
            return administrator.objects.get(gmailId=email)
        except:
            return False

    @staticmethod
    def get_administrator_by_email_password(email, password):
        try:
            return administrator.objects.get(gmailId=email, mobileNo=password)
        except:
            return False


class department(models.Model):
    departmentName = models.CharField(max_length = 20)
    description = models.CharField(max_length = 50)

    def __str__(self):
        return self.departmentName

    @staticmethod
    def get_department_by_id(id):
        try:
            if id:
                return department.objects.get(id=id)
            else:
                return department.objects.all()
        except:
            return False


class faculty(models.Model):
    name = models.CharField(max_length = 50)
    designation = models.CharField(max_length = 50)
    gmailId = models.CharField(max_length = 50)
    mobileNo = models.CharField(max_length = 50)
    departmentId = models.ForeignKey(department, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    @staticmethod
    def get_faculty_by_id(id):
        try:
            return faculty.objects.get(id=id)
        except:
            return False

    @staticmethod
    def get_faculty_by_email(email):
        try:
            return faculty.objects.get(gmailId=email)
        except:
            return False

    @staticmethod
    def get_faculty_by_mobileNumber(number):
        try:
            return faculty.objects.get(mobileNo=number)
        except:
            return False

    @staticmethod
    def get_faculty_by_email_password(email, password):
        try:
            return faculty .objects.get(gmailId=email, mobileNo=password)
        except:
            return False


    @staticmethod
    def get_faculty_by_department_id(id):
        try:
            return faculty.objects.filter(departmentId=id)
        except:
            return False

    @staticmethod
    def get_department_by_facultyId(id):
        try:
            return faculty.objects.get(id=id)
        except:
            return False


class course(models.Model):
    courseName = models.CharField(max_length = 20)
    description = models.CharField(max_length = 50)
    departmentId = models.ForeignKey(department, on_delete = models.CASCADE)

    def __str__(self):
        return self.courseName

    @staticmethod
    def get_course_by_id(id):
        try:
            return course.objects.get(id=id)
        except:
            return False

    @staticmethod
    def get_course_by_department_id(id):
        try:
            return course.objects.filter(departmentId=id)
        except:
            return False


class semester(models.Model):
    semester = models.CharField(max_length = 5)

    def __str__(self):
        return self.semester

    @staticmethod
    def get_semester_by_id(id):
        try:
            return semester.objects.get(id=id)
        except:
            return False


class student(models.Model):
    studentName = models.CharField(max_length = 50)
    courseId = models.ForeignKey(course, on_delete = models.CASCADE)
    semesterId = models.ForeignKey(semester, on_delete = models.CASCADE)
    departmentId = models.ForeignKey(department, on_delete = models.CASCADE)

    def __str__(self):
        return self.studentName

    @staticmethod
    def get_student_by_id(id):
        try:
            return student.objects.get(id=id)
        except:
            return False

    @staticmethod
    def get_student_by_course_id_semester_id(courseId, semesterId):
        try:
            return student.objects.filter(courseId=courseId, semesterId=semesterId)
        except:
            return False

    @staticmethod
    def get_student_count_by_department_id(departmentId):
        try:
            return student.objects.filter(departmentId=departmentId).count()
        except:
            return False

    @staticmethod
    def get_student_by_department_id(departmentId):
        try:
            return student.objects.filter(departmentId=departmentId)
        except:
            return False


class subject(models.Model):
    subjectName = models.CharField(max_length = 50)
    courseId = models.ForeignKey(course, on_delete = models.CASCADE)
    semesterId = models.ForeignKey(semester, on_delete = models.CASCADE)
    departmentId = models.ForeignKey(department, on_delete = models.CASCADE)

    def __str__(self):
        return self.subjectName

    @staticmethod
    def get_subject_by_id(id):
        try:
            return subject.objects.get(id=id)
        except:
            return False

    @staticmethod
    def get_subject_by_department_id(departmentId):
        try:
            return subject.objects.filter(departmentId=departmentId)
        except:
            return False

    @staticmethod
    def get_subject_by_semester_id(semesterId):
        try:
            return subject.objects.filter(semesterId=semesterId)
        except:
            return False

    @staticmethod
    def get_subject_by_course_id_semester_id(courseId, semesterId):
        try:
            return subject.objects.filter(courseId=courseId, semesterId=semesterId)
        except:
            return False


class attendanceDetails(models.Model):
    courseId = models.ForeignKey(course, on_delete = models.CASCADE)
    semesterId = models.ForeignKey(semester, on_delete = models.CASCADE)
    subjectId = models.ForeignKey(subject, on_delete = models.CASCADE)
    facultyId = models.ForeignKey(faculty, on_delete = models.CASCADE)
    date = models .DateField()

    # def __str__(self):
    #     return self

    @staticmethod
    def get_attendance_list_by_id(id):
        try:
            return attendanceDetails.objects.get(id=id)
        except:
            return False

    @staticmethod
    def get_attendance_list_by_faculty_id(id):
        try:
            return attendanceDetails.objects.filter(facultyId=id)
        except:
            return False

    @staticmethod
    def get_attendance_list_by_course_semester_subject(courseId, semesterId, subjectId):
        try:
            return attendanceDetails.objects.filter(courseId=courseId, semesterId=semesterId, subjectId=subjectId)
        except:
            return False

    @staticmethod
    def get_attendance_list_by_faculty_course_semester_subject(facultyId, courseId, semesterId, subjectId):
        try:
            return attendanceDetails.objects.filter(facultyId=facultyId, courseId=courseId, semesterId=semesterId, subjectId=subjectId)
        except:
            return False

    @staticmethod
    def get_class_count_by_faculty_id(id):
        try:
            return attendanceDetails.objects.filter(facultyId=id).count()
        except:
            return False


class attendance(models.Model):
    studentRollNo = models.ForeignKey(student, on_delete = models.CASCADE)
    action = models.CharField(max_length = 1, default="A")
    attendanceDetailsId = models.ForeignKey(attendanceDetails, on_delete = models.CASCADE)

    @staticmethod
    def get_student_by_attendance_id(id):
        try:
            return attendance.objects.filter(attendanceDetailsId=id)
        except:
            return False

    @staticmethod
    def get_all_student_by_attendance_id(id):
        try:
            return attendance.objects.filter(attendanceDetailsId=id).count()
        except:
            return False

    @staticmethod
    def get_present_student_by_action(id):
        try:
            return attendance.objects.filter(attendanceDetailsId=id, action="P").count()
        except:
            return False

    @staticmethod
    def get_total_attendance_count_by_studnet(id):
        try:
            return attendance.objects.filter(studentRollNo=id).count()
        except:
            return False

    @staticmethod
    def get_present_attendance_count_by_studnet(id):
        try:
            return attendance.objects.filter(studentRollNo=id, action="P").count()
        except:
            return False

    @staticmethod
    def get_total_attendance_count_by_studnet_attendanceList(studentList, attendanceList):
        try:
            return attendance.objects.filter(studentRollNo=studentList, attendanceDetailsId=attendanceList).count()
        except:
            return False

    @staticmethod
    def get_present_attendance_count_by_studnet_attendanceList(studentList, attendanceList):
        try:
            return attendance.objects.filter(studentRollNo=studentList, attendanceDetailsId=attendanceList, action="P").count()
        except:
            return False