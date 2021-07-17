from football_api.database import db

class Team(db.Model):
    """
    Team Flask-SQLAlchemy Model
    Represents objects contained in the teams table
    """
    ___tablename__ = "teams"
    team_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(),unique=True, nullable=False)
    abbreviations = db.Column(db.String(), unique=True, nullable=False)