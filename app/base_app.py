from flask import (
      Blueprint, flash, g, redirect, render_template, request, url_for,session
)
from werkzeug.exceptions import abort

# from jobapp.auth import login_required
# # from jobapp.models import get_db

bp = Blueprint('home', __name__)

from .models import enquires, db

@bp.route('/', methods=('get', 'post'))
def index():

      if request.method == 'POST':
            fullname = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            subject = request.form['subject']
            body = request.form['message_body']
            try:
                  enquiry_to_send = enquires(
                        fullname = fullname,
                        email = email,
                        phone = phone,
                        subject = subject,
                        body = body
                  )
                  print('adding data to commit')

                  db.session.add(enquiry_to_send)

                  print('Data added to commit')
                  print('Storing data to database')

                  db.session.commit()

                  print('Data added to database sucessfully')
            except:
                  # flash(message="Email has been  sent successfully", category='info')
                  print('There was an error')
      
      return render_template('index.html')

@bp.route('/about')
def aboutPage():


      return render_template('about.html')

@bp.route('/services')
def servicesPage():


      return render_template('services.html')

@bp.route('/register-student')
def registerPage():


      return render_template('register.html')

@bp.route('/contact-us')
def contactPage():


      return render_template('contact.html')



# 
# 
#
import babel

# @bp.app_template_filter()
# def format_datetime(value, format='medium'):
#       if format== 'full':
#             format = 'EEEE, d. MMMM y "at" HH:mm'
#       elif format == 'medium':
#             format = "EE dd.MM.y HH:mm"
#       return babel.dates.format_timedelta(value, format)