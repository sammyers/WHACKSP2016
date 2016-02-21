''' Returns a list of all posible combinations'''
from models import Idea
from database import db_session
import itertools

ideas = Idea.query.all()

names = [idea.name for idea in ideas]

def combine(vals):
    values = list(itertools.combinations(vals,2))
    print values

combine(names)

