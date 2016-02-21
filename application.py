from flask import render_template, request, redirect, flash, session, url_for
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from app import application
from app.database import db_session
from app.forms import VoteForm, SubmitForm
from app.models import Idea
import random, json

application.secret_key = '23456787654'
application.debug = True

class MyForm(Form):
    name = StringField('submit new idea', validators=[DataRequired()])

@application.route('/', methods=['GET', 'POST'])
def index():
    form1 = MyForm(request.form)
    if request.method == 'POST' and form1.validate_on_submit():
        new_idea_str = form1.name.data
        new_idea = Idea(new_idea_str)

        db_session.add(new_idea)
        db_session.commit()
        
        return redirect('/')
    return render_template('index.html',  form1=form1)


@application.route('/vote') # homepage URL endpoint
def vote():
    string = 'Pick Between these 2 ideas'
    db_ideas = Idea.query.all()
    all_ideas = json.dumps({idea.id: idea.name for idea in db_ideas})
    return render_template('voting.html', ideas=all_ideas)


@application.route('/rankings') # homepage URL endpoint
def ratings():
    sorted_ideas = Idea.query.order_by(Idea.passes.asc()).all()

    return render_template('rating.html', lists=sorted_ideas)


@application.route('/about')
def about():
    return render_template('about.html')


@application.route('/objectvoting',methods = ['GET','POST'])
def objectvoting():
    voting = VoteForm(request.form)
    submission = SubmitForm(request.form)
    all_ideas = Idea.query.all()
    #two_objects = #Ian's method for two objects
    left_object = random.choice(all_ideas)
    right_object = random.choice(all_ideas)
    while left_object == right_object:
        right_object = random.choice(all_ideas)
    #then allow for clicking and choosing which one to vote
    return render_template('index.html', left_object=left_object, 
                                         right_object=right_object,
                                         voting=voting,
                                         submission=submission)



if __name__ == '__main__':
    application.run(debug=True)
