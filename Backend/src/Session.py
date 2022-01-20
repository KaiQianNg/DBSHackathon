from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from dotenv import dotenv_values

loc = os.path.join(os.path.dirname(os.path.realpath(__file__)).split('src')[0],'.env')
os_config = dotenv_values(loc)
SQLALCHEMY_DATABASE_URI = os_config['SQLALCHEMY_DATABASE_URI']
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=engine))
