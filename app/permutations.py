''' Returns a list of all posible combinations'''
from models import Idea
from database import db_session
import itertools

ideas = Idea.query.all()

names = [idea.name for idea in ideas]
ids = [idea.id for idea in ideas]

def giveNames():
    for i in range(len(names)):
        res = res.append(list(names[i] + ids[i]))

# def combine(vals):
#     values = list(itertools.combinations(vals,2))
#     print values

# def combinations(iterable, r):
#     # combinations('ABCD', 2) --> AB AC AD BC BD CD
#     # combinations(range(4), 3) --> 012 013 023 123
#     pool = tuple(iterable)
#     n = len(pool)
#     if r > n:
#         return
#     indices = list(range(r))
#     yield tuple(pool[i] for i in indices)
#     while True:
#         for i in reversed(range(r)):
#             if indices[i] != i + n - r:
#                 break
#         else:
#             return
#         indices[i] += 1
#         for j in range(i+1, r):
#             indices[j] = indices[j-1] + 1
#         yield list(pool[i] for i in indices) #uses list not tuple

# combine(names)

