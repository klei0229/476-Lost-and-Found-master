# getting Form from flask_wtf
from flask_wtf import Form
# getting the input fields from wtfroms
from wtforms import StringField, PasswordField, SubmitField
# getting validators properties
from wtforms.validators import DataRequired, Email, Length
# class to sign up
class SignupForm(Form):
    #the field for first name
  first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
    # the field for last name
  last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
    # the field for email
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
    # the field for passowrd
  password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])
    # the field for sumbit to signup
  submit = SubmitField('Sign up')

# class for login
class LoginForm(Form):
    # username
	email = StringField('Email' , validators = [DataRequired("Please enter your email address") , Email("Please enter your email address")])
    # password
	password = PasswordField('Password', validators= [DataRequired("Please enter a password")])
    # sumbit 
	submit = SubmitField("Sign In")
