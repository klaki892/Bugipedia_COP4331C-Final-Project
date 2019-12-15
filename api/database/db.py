import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from flask import current_app as app

def getSession( user, passwd):

    if not os.getenv("DATABASE_URL"):
        raise RuntimeError("DATABASE_URL is not set")

    Session = sessionmaker(autocommit=False,
                           autoflush=False,
                           bind=create_engine(os.getenv("DATABASE_URL"))
                          )
    return scoped_session(Session)
