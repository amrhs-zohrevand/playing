def __init__(self, card_id, user):
    self.card_id = card_id
    self.user = user


def __init__(self, user_id):
    self.user_id = user_id


with open("data.csv", 'rb') as f:
    reader = csv.reader(f)
    chunk = list(reader)

cards = []
for one_row in chunk:
    user = cr.User.from_one_row(one_row)
    card = cr.Card.from_one_row(one_row,user)
    cards.append(card)

try:
    # 3 - create a new session
    session = Session()

    # cards = qr.from_csv('data.csv')

    for card in cards:
        session.add(card)

    session.commit()
finally:
    session.close()

from example_orm import query as qr
from example_orm import card as cr