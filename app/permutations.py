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
<<<<<<< HEAD
=======
#print(itertools.combinations(['test','test2','test3','test4','test5','test6','test7','test8'], 2))
>>>>>>> 12cec98303573e94c9f9574ea5d751a282460923
