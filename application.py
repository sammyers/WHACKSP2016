from flask import render_template, request, redirect, flash, session, url_for
from flask_wtf import Form
from app import application
from app.database import db_session
from app.forms import VoteForm, SubmitForm
from app.models import Idea
import random

@application.route('/') # homepage URL endpoint
def index():
	string = 'Hello World'
	return render_template('index.html', hello=string)

@application.route('/objectvoting',methods = ['GET','POST'])
def objectvoting():
	voting = VoteForm(request.form)
	submission = SubmitForm(request.form)
	all_ideas = Idea.query.all()
	#two_objects = #Ian's method for two objects
	left_object = two_objects[0]
	right_object = two_objects[1]
	#then allow for clicking and choosing which one to vote
	return render_template('index.html', left_object=left_object, 
										 right_object=right_object,
										 voting=voting,
										 submission=submission)

@application.route('/votevotevote', methods = ['POST'])
def votevotevote():
	#after clicked, will run an algorithm that increments the vote as well as update ELO ratings

	idea1 = str(request.form['votingbutton'])

	return redirect('/')

@application.route('/add-data')
def add_data():
	return render_template('add_data.html')

if __name__ == '__main__':
	application.run(debug=True)
