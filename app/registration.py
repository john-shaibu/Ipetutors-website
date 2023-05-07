
from flask import (
      Blueprint, flash, g, redirect, render_template, request, url_for
)
# from werkzeug.exceptions import abort

# from jobapp.auth import login_required

from app.models import db, student_applications

bp = Blueprint('registration', __name__, url_prefix='/register')


@bp.route('/', methods=('GET', 'POST'))
def register():

      if request.method == "GET":

            registrationOption = request.args['registration_options']

            if registrationOption == 'student':                
                  registrationType="student"
            else:
                  registrationType="tutor"

            

      return render_template('register.html', registrationType=registrationType)

@bp.route('/register-sucess', methods=('GET', 'POST'))
def studentRegister():

      if request.method == 'POST':
             
            registrationData =  student_applications(
                  firstname = request.form['firstname'],
                  lastname = request.form['lastname'],
                  othernames = request.form['othername'],
                  state = request.form['stateOfOrigin'],
                  lga = request.form['lga'],
                  age = request.form['age'],
                  marital_status = request.form['marital_status'],
                  gender = request.form['gender'],
                  address = request.form['address'],
                  phone_number = request.form['phone'],
                  email = request.form['email'],
                  guardian_fullname = request.form['guardian_fullname'],
                  guardian_occupation = request.form['guardian_occupation'],
                  guardian_phone_number = request.form['guardian_phone_number'],
                  guardian_email = request.form['guardian_email'],
                  guardian_address = request.form['guardian_address'],
                  teaching_mode = request.form['teaching_type'],
                  topics_or_subject = request.form['topics_or_subject'],
                  difficulties = request.form['problem_subject'],
                  additional_information = request.form['additional_information'],

            )
            print('adding data to commit')

            db.session.add(registrationData)

            print('Data added to commit')
            print('Storing data to database')

            db.session.commit()

            print('Data added to database sucessfully')


            print(registrationData)

            

      return render_template('register_success.html')

# @bp.route('/p/requirement', methods=('GET', 'POST'))
# def job_requirement():

#       if request.method == 'POST':
            
#             return redirect(url_for('recruiter.job_description'))

#       return render_template('recruiter/job_requirement.html')

# @bp.route('/p/description', methods=('GET', 'POST'))
# def job_description():

#       if request.method == 'POST':
            
#             return redirect(url_for('recruiter.job_compensation'))

#       return render_template('recruiter/job_description.html')

# @bp.route('/p/compensation', methods=('GET', 'POST'))
# def job_compensation():

#       if request.method == 'POST':
            
#             return redirect(url_for('recruiter.job_preference'))

#       return render_template('recruiter/job_compensation.html')

# @bp.route('/p/preference', methods=('GET', 'POST'))
# def job_preference():

#       return render_template('recruiter/job_preference.html')

# @bp.route('/username')
# def recruiter_profile():


#       return render_template('recruiter/recruiter_profile.html')