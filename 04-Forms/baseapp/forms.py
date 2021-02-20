from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class BookmarkForm(FlaskForm):
    title       = StringField('Title' , validators=[DataRequired(message='Please enter Title.')])
    description = StringField('Description' , validators=[DataRequired(message='Please capture description.')])
    category    = StringField('Category' , validators=[DataRequired(message='Please enter Category.')])
    link        = StringField('Link' , validators=[DataRequired(message='Please add bookmark link.'), URL(require_tld=True, message='Enter a valid URL')])
    create      = SubmitField('Save')