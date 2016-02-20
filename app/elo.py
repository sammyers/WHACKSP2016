""" Expects to be able to find 2 ratings from the database """
"""depricated"""

#Picks the two relevant nodes from the database based on some criteria to give everything a chance.
ideas = whack2016.query.all()

#ideas_ranked = db.session.query(whack2016).order_by(idea.votes.desc())

factor = len(ideas)/4
validIdeas = db.session.query.filter(Idea.passed < factor).order_by(Idea.elo.asc()).all()
#returns a list of all ideas that meet requirements, ordered by elo 

names = [idea.name for idea in ideas] #how to get mah shit




#Things I want
#drop all that have been rejecteded more than n times, when n is based on list length
#vote on any 2 of the remaining, picking one randomly, and an adjacent one

#define views
k = 30 /( (views/10).floor() + 1)# effect of each result on scoring, dynamic based on number of views

#should be a function to call from the database
r1 = 10 #this should be the rating of some idea in the database.
r2 = 10 #this should be the rating of the comparable idea in the database.

# function to build expectation (probably automatically run within something else)
e1 = 1/(1 + 10**((r1-r2)/400)) # expected chance r1 will win the vote
e2 = 1/(1 + 10**((r2-r1)/400)) # expected chance r2 will win the vote

# Determine who wins here

# Define rwinner and loser in terms of r1 and r2 and create ewinner and eloser in terms of e1 e2

#function to build rating changes
rwinnernew = rwinner + k * (1 - ewinner)
rlosernew = rloser + k (0 - eloser)

#update the database with rwinnernew and rlosernew to their correct spots
