from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FloatField, RadioField
from wtforms.validators import DataRequired, InputRequired, ValidationError, Email, EqualTo
from app.models import User


class SubmissionForm(FlaskForm):
    number = FloatField('First Number:', validators=[InputRequired()])
    number2 = FloatField('Second Number:', validators=[InputRequired()])
    operator = RadioField('Operator:', choices =[('add', 'Add'), ('subtract','Subtract'),
                                                  ('multiply', 'Multiply'), ('divide', 'Divide')], 
                                                  validators=[DataRequired()])
    submit = SubmitField('Submit Entry')