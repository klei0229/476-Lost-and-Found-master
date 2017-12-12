# using the flask sql
from flask.ext.sqlalchemy import SQLAlchemy
# getting the hash ability
from werkzeug import generate_password_hash, check_password_hash
# set out the database
db = SQLAlchemy()

#class for database
class User(db.Model):
    # the name of table
  __tablename__ = 'users'
  # the properties of table: ID, first name , last name, email, password with hash
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))
  # the inti for this class.
  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)
    # the function for setting the passowrd
  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)

    # the function to check the password 
  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)
