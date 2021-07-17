from football_api.database import db

class Team(db.Model):
    """
    Team Flask-SQLAlchemy Model
    Represents objects contained in the teams table
    """
    ___tablename__ = "teams"