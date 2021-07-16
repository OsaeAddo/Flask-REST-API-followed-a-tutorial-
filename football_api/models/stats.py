from football_api.database import db

class Stats(db.Model):
    """
    Stats Flask-SQLAlchemy Model
    Represents objects contained in the stats table
    """
    stat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(db.Integer, ForeignKey("players.player_id"), nullable=False)
    season = db.Column(db.Integer, ForeignKey("seasons.year"), nullable=False)
    team_id = db.Column(db.Integer, ForeignKey("teams.team_id"), nullable=False)

    age = db.Column(db.Integer, nullable=False)
    games = db.Column(db.Integer, nullable=False)
    games_started = db.Column(db.Integer, nullable=False)
    completions = db.Column(db.Integer)
    pass_attempts = db.Column(db.Integer)
    pass_yards = db.Column(db.Integer)
    pass_tds = db.Column(db.Integer)
    interceptions = db.Column(db.Integer)
    rush_attempts = db.Column(db.Integer)
    rush_yards = db.Column(db.Integer)
    rush_yards_per_attempt = db.Column(db.Float)
    rush_tds = db.Column(db.Integer)
    targets = db.Column(db.Integer)
    receptions = db.Column(db.Integer)
    rec_yards = db.Column(db.Integer)
    fumbles = db.Column(db.Integer)