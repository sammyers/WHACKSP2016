from sqlalchemy import Column, Integer, String, Numeric
from database import Base
    
class Idea(Base):
    
    __tablename__ = 'ideas'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True)
    elo = Column(Numeric)
    views = Column(Integer)
    passes = Column(Integer)

    def __init__(self, name=None, elo=1000, views=0, passes=0):
        self.name = name
        self.elo = elo
        self.views = views
        self.passes = 0

    def __repr__(self):
        return '<Idea {} Elo {} Views {} Passes {}>'.format(self.name, self.elo, self.views, self.passes)