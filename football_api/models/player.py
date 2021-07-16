from football_api.database import db

class Player(db.Model):
    """
    Player Flask-SQLAlchemy Model
    Represents objects contained in the players table
    """
    __tablename__ = "players"

    player_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=True)
    position = db.Column(db.String(), nullable=False)
    