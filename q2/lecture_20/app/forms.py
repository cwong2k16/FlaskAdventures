from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FloatField, RadioField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User


class SubmissionForm(FlaskForm):
    number = FloatField('First Number:', validators=[DataRequired()])
    number2 = FloatField('Second Number:', validators=[DataRequired()])
    operator = RadioField('Operator:', choices =[('add', 'Add'), ('subtract','Subtract'),
                                                  ('multiply', 'Multiply'), ('divide', 'Divide')])
    submit = SubmitField('Submit Entry')