from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField

class VoteForm(Form):
	firstitem = SubmitField('Vote')
	seconditem = SubmitField('Vote')

class SubmitForm(Form):
	entry = TextAreaField()
	submit = SubmitField('Submit')
