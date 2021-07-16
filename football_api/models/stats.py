from football_api.database import db

class Stats(db.Model):
    """
    Stats Flask-SQLAlchemy Model
    Represents objects contained in the stats table
    """
    stat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(db.Integer, primary_key("players.player_id"), nullable=False)
    