from flask import render_template

from app import application
from app.database import db_session

@application.route('/') # homepage URL endpoint
def index():
	string = 'Hello World'
	return render_template('index.html', hello=string)

@application.route('/voting')
def ideavote():
	#will pull two objects from the database
	#then allow for clicking and choosing which one to vote
	#after clicked, will run an algorithm that increments the vote as well as update ELO ratings
	#will check to see if one of the objects has passed the upvote threshold
	#if yes, then return rankings screen
	#if no, then re-run this code
    pass

if __name__ == '__main__':
	application.run(debug=True)
