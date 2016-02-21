from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.constants import DB_URI

engine = create_engine(DB_URI, convert_unicode=True, pool_recycle=60, pool_size=20)
db_session = scoped_session(sessionmaker(autocommit=False, 
										 autoflush=False, 
										 bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
	import models
	Base.metadata.create_all(bind=engine)
