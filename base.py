# CREATE DATABASE orm_test CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib import quote_plus as urlquote
import codecs
import platform


codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

password = "DAEAS@daeas67" if platform.system() == 'Windows' else "daeasdaeas"

engine = create_engine('mysql+mysqlconnector://root:%s@localhost/orm_test?charset=utf8mb4' % urlquote(password), echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()
