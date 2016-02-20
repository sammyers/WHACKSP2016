from flask import render_template, request, redirect, flash, session, url_for

from flask_wtf import Form
from app import application
from app.database import db_session

@application.route('/') # homepage URL endpoint
def index():
	string = 'Hello World'
	return render_template('index.html', hello=string)

@application.route('/objectvoting',methods = ['GET','POST'])
def objectvoting():
	#will pull two objects from the database
	two_objects = [("chicken1","chicken2"), ("chicken3, chicken2"),("chicken1", "chicken3")]
	#two_objects = #Ian's method for two objects
	left_object, right_object = two_objects[0]
	two_objects
	#then allow for clicking and choosing which one to vote
	return render_template('index.html', left_object = left_object, right_object = right_object)

@application.route('/votevotevote', methods = ['POST'])
def votevotevote():
	#after clicked, will run an algorithm that increments the vote as well as update ELO ratings

	idea1 = str(request.form['votingbutton'])

	#increment voting for the winner

	

	return redirect("/objectvoting")



if (__name__ == '__main__'):
	application.run(debug=True)
