import os

from flask import Flask


def create_app():
      app = Flask(__name__)

      app.config['SECRET_KEY'] = '54092193f0caed73cc9b663328fb561a'
      app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ipetutors.db'
      app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
      
      from app.models import db
      db.init_app(app)

      with app.app_context():
            db.create_all()

      #register the authentication blueprint from auth.py to our factory
      # from . import auth
      # app.register_blueprint(auth.bp)

      #register the job blueprint from job.py to our factory
      from . import base_app
      app.register_blueprint(base_app.bp)
      app.add_url_rule('/', endpoint='index')

      #register the admin blueprint from admin.py to our factory
      from . import admin
      app.register_blueprint(admin.bp)

      #register the recruiter blueprint from job.py to our factory
      from . import registration
      app.register_blueprint(registration.bp)

      return app