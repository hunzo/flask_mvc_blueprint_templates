from . import db
from datetime import datetime


class TokenInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return 'id: {}, username: {}, created: {}'.format(self.id, self.username, self.created)
