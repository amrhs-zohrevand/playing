import csv
from base import Session, engine, Base

from sqlalchemy import Column, Integer, ForeignKey, Table, MetaData
from sqlalchemy.orm import relationship
from base import Base

def create_cards_table():

    metadata = MetaData()
    cards = Table('cards', metadata,
                   Column("card_id", Integer, primary_key=True),
                  Column("user_id", Integer),
                   # Column(Integer, ForeignKey("users.user_id")),
                   )
    return cards


def create_users_table():

    metadata = MetaData()
    users = Table('users', metadata,
                   # Column("card_id", Integer, primary_key=True),
                  Column("user_id", Integer, primary_key=True),
                   # Column(Integer, ForeignKey("users.user_id")),
                   )
    return users


class Card:

    def __init__(self, card_id, user_id):
        self.card_id = card_id
        self.user_id = user_id


class User:

    def __init__(self, user_id):
        self.user_id = user_id


# 2 - generate database schema
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

user0.__dict__.keys()

dir(user0)

attrs = vars(card)

print ', '.join("%s: %s" % item for item in attrs.items())

map(vars, cards_all)

inserter = table_object.insert().prefix_with("OR REPLACE")


from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import Insert

@compiles(Insert)
def append_string(insert, compiler, **kw):
    s = compiler.visit_insert(insert, **kw)
    if 'append_string' in insert.kwargs:
        return s + " " + insert.kwargs['append_string']
    return s


my_connection.execute(my_table.insert(append_string = 'ON DUPLICATE KEY UPDATE foo=foo'), my_values)


try:
    # 3 - create a new session
    session = Session()

    # cards = qr.from_csv('data.csv')
    session.add_all(users_all)
    for card in cards_all:

        session.add(card)

    session.commit()
finally:
    session.close()





# class User(Base):
#     __tablename__ = 'users'
#     user_id = Column(Integer, primary_key=True)
#     # card_id = Column(ForeignKey("cards.card_id"), nullable=False)
#     # cards = relationship("Card", back_populates="user")
#     # card = relationship("Card", backref="users")


# class Card(Base):
#     __tablename__ = 'cards'
#
#     card_id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.user_id"))
#     # user = relationship("User", back_populates="cards")
#     # user = relationship("User", backref="cards")

# class User:
#     # __tablename__ = 'users'
#     # user_id = Column(Integer, primary_key=True)
#     # card_id = Column(ForeignKey("cards.card_id"), nullable=False)
#     # cards = relationship("Card", back_populates="user")
#     # card = relationship("Card", backref="users")
#
#     def __init__(self, user_id):
#         self.user_id = user_id