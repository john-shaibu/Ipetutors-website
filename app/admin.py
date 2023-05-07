from flask import (
      Blueprint, flash, g, redirect, render_template, request, url_for,session
)

bp = Blueprint('admin', __name__, url_prefix='/admin')

from app.models import db, student_applications

@bp.route('/')
def  dashboard():

      registeredStudents = student_applications.query.all()

      return render_template('/admin/admin_dashboard.html', students = registeredStudents)

@bp.route('/admin-login', methods=('GET', 'POST'))
def  adminLogin():

      return render_template('/admin/admin_login.html')

@bp.route('/students', methods=('GET', 'POST'))
def  registeredStudents():

      registeredStudents = student_applications.query.order_by(student_applications.date.desc()).all()

      return render_template('/admin/registered_students.html', students = registeredStudents)

# ==================================================================
# ==================================================================
# ==================================================================
# ==================================================================

@bp.route('/students/<int:id>/message', methods=('GET', 'POST'))
def  sendStudentMessage(id):

      student_to_send_message = student_applications.query.filter_by(id=id)

      return render_template('/admin/send_student_message.html', student_to_send_message=student_to_send_message)

@bp.route('/students/<int:id>/request-payment', methods=('GET', 'POST'))
def  requestPayment(id):

      student_to_request_payment_from = student_applications.query.filter_by(id=id)

      if request.method == "POST":

            if request.form['email_or_phone'] == "email":
                  email_or_phone = request.form['user_email']
            else :
                  email_or_phone = request.form['user_phone']
                  

            recipient  = email_or_phone
            payment_for = request.form['payment_for']
            amount = request.form['amount']
            additional_information = request.form['information']
            
            print(recipient, payment_for, amount, additional_information)

            flash(message='Payment request sent successfully', category='message')

            import time

            time.sleep(5.0)

            return redirect('admin.registeredStudents')




      return render_template('/admin/student_payment_request.html', 
                             student_to_request_payment_from=student_to_request_payment_from)



@bp.route('/registered-teachers', methods=('GET', 'POST'))
def  registeredTeachers():

      return render_template('/admin/registered_teachers.html')

@bp.route('/student-application', methods=('GET', 'POST'))
def  appliedStudents():

      return render_template('/admin/student_application_info.html')

@bp.route('/students/<int:id>/', methods=('GET', 'POST'))
def  studentsInfo(id):

      studentInfo = student_applications.query.filter_by(id=id)

      return render_template('/admin/student_application_info.html', studentInfo = studentInfo)

@bp.route('/enquires', methods=('GET', 'POST'))
def  enquires():

      return render_template('/admin/enquires.html')

@bp.route('/settings', methods=('GET', 'POST'))
def  adminPage():

      return render_template('/admin/admin_page.html')