from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):
    title = StringField('Review title', validators = [Required()])
    review = TextAreaField('Movie Review')
    submit = SubmitField('Submit')

    # review = TextAreaField('Movie Review', validators = [Required()])

#edit profile
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you:', validators = [Required()])
    submit = SubmitField('Submit')
