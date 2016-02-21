from sqlalchemy import Column, Integer, String, Numeric, Text
from app.database import Base
    
class Idea(Base):
    
    __tablename__ = 'ideas'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True)
    elo = Column(Numeric)
    votes = Column(Text)
    views = Column(Integer)
    passes = Column(Integer)

    def __init__(self, name=None, elo=1000, votes=0, views=0, passes=0):
        self.name = name
        self.elo = elo
        self.votes = votes
        self.views = views
        self.passes = passes

    def __repr__(self):
        return '<Idea {} Elo {} Views {} Passes {}>'.format(self.name, self.elo, self.views, self.passes)
