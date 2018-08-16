# General note! Not efficient at all!
# The ON DUPLICATE is not available at all in ORM layer
# First issues a SELECT statement which would be time consuming

import csv
from base import Session, engine, Base

from sqlalchemy import Column, Integer, ForeignKey, Table, MetaData
from sqlalchemy.orm import relationship
from base import Base

# 1 - create classes with base
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    # card_id = Column(ForeignKey("cards.card_id"), nullable=False)
    # cards = relationship("Card", back_populates="user")
    # card = relationship("Card", backref="users")


class Card(Base):
    __tablename__ = 'cards'

    card_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    # user = relationship("User", back_populates="cards")
    # user = relationship("User", backref="cards")


# 2 - generate database schema
# Note: Before this, check if the DB exists! Refer to base.py
# Base.metadata.create_all(engine)

with open("data.csv", 'rb') as f:
    reader = csv.reader(f)
    chunk = list(reader)

cards_all = []
users_all = []
for one_row in chunk:
    # user0 = User(user_id=int(one_row[0]))
    user0 = User(user_id=int(one_row[0]))
    users_all.append(user0)

    card = Card(card_id=int(one_row[1]), user_id=int(one_row[0]))
    cards_all.append(card)


# In case I need a mapper
kw_map = {a.key: a.class_attribute.name for a in User.__mapper__.attrs}

kwargs = {a.key: user0[a.class_attribute.name] for a in User.__mapper__.attrs}

try:
    # 3 - create a new session
    session = Session()

    # users_all = session.merge(users_all)

    merged_users = map(session.merge, users_all)
    # cards = qr.from_csv('data.csv')
    session.add_all(merged_users)
    for card in cards_all:
        session.add(card)

    session.commit()
finally:
    session.close()

