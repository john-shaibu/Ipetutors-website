
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class students(db.Model):
      id = db.Column(db.Integer, primary_key=True, autoincrement=True)
      firstname = db.Column(db.String(60), nullable = False)
      lastname = db.Column(db.String(60), nullable = False)
      othernames = db.Column(db.String(60))
      state = db.Column(db.String(60))
      lga = db.Column(db.String(60))
      age = db.Column(db.String(20))
      marital_status = db.Column(db.String(20), nullable = False)
      gender = db.Column(db.String(20), nullable = False)
      address = db.Column(db.String(100), nullable = False)
      phone_number = db.Column(db.String(20), nullable = False)
      email = db.Column(db.String(60), nullable=False, unique=True)
      guardian_fullname = db.Column(db.String(60), nullable=False)
      guardian_occupation = db.Column(db.String(60), nullable=False)
      guardian_phone_number = db.Column(db.String(20), nullable=False)
      guardian_email = db.Column(db.String(60))
      guardian_address = db.Column(db.String(100), nullable=False)
      teaching_mode = db.Column(db.String(60), nullable=False)
      admission_status = db.Column(db.String(60), nullable=False, default='Not yet admitted')
      topics_or_subject = db.Column(db.String(60), nullable=False)
      date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
      difficulties = db.Column(db.String(200), nullable=False, default = 'No difficulties')
      additional_information = db.Column(db.String(400), nullable = False, default = "No additional information")

      def __repr__(self):
            return f"students('{self.firstname}', '{self.lastname}')"

class student_applications(db.Model):
      id = db.Column(db.Integer, primary_key=True, autoincrement=True)
      firstname = db.Column(db.String(60), nullable = False)
      lastname = db.Column(db.String(60), nullable = False)
      othernames = db.Column(db.String(60))
      state = db.Column(db.String(60))
      lga = db.Column(db.String(60))
      age = db.Column(db.String(20))
      marital_status = db.Column(db.String(20), nullable = False)
      gender = db.Column(db.String(20), nullable = False)
      address = db.Column(db.String(100), nullable = False)
      phone_number = db.Column(db.String(20), nullable = False)
      email = db.Column(db.String(60), nullable=False, unique=True)
      guardian_fullname = db.Column(db.String(60), nullable=False)
      guardian_occupation = db.Column(db.String(60), nullable=False)
      guardian_phone_number = db.Column(db.String(20), nullable=False)
      guardian_email = db.Column(db.String(60))
      guardian_address = db.Column(db.String(100), nullable=False)
      teaching_mode = db.Column(db.String(60), nullable=False)
      admission_status = db.Column(db.String(60), nullable=False, default='admitted')
      topics_or_subject = db.Column(db.String(60), nullable=False)
      date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
      difficulties = db.Column(db.String(200), nullable=False, default = 'No difficulties')
      additional_information = db.Column(db.String(400), nullable = False, default = "No additional information")

      def __repr__(self):
            return f"User('{self.firstname}', '{self.lastname}')"

class enquires(db.Model):
      id = db.Column(db.Integer(), primary_key = True, autoincrement = True)
      status = db.Column(db.String(20), nullable=False, default = 'unreplied')
      fullname = db.Column(db.String(60), nullable=False, default = 'no name provided')
      email = db.Column(db.String(60), nullable=False, default = 'no email provided')
      phone = db.Column(db.String(60), nullable=False, default = 'no phone provided')
      subject = db.Column(db.String(120), nullable=False, default = 'no subject provided')
      body = db.Column(db.String(800), nullable=False, default = 'no content provided')

      def __repr__(self):
            return f"enquires('{self.subject}', '{self.body})"