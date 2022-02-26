import email
from flask import Flask
from wtforms import SubmitField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename

class UploadForm(FlaskForm):
    photo = FileField(validators=[FileRequired(), FileAllowed(['png', 'jpg'], "wrong format!")])
    submit = SubmitField('Upload')