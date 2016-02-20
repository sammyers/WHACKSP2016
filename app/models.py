from application import db
    
    class Idea(db.Model):

        __tablename__ = 'ideas'

        id = Column(Integer, primary_key=True, index=True)
        name = Column(string(255), unique=True)
        elo = Column(Numeric, asdecimal=False)
        views = Column(Integer)
        passes = Column(Integer)

        def __init__(self, name=None, elo=1000, views=0, passes=0):
            self.name = name

        def __repr__(self):
            return '<Idea %i Elo %e Views %v Passes%p>' %(self.name, self.elo, self.views self.passes)


