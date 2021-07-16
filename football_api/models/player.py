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

    stats = db.relationship("Stats", back_populated="player")

    #Define how player should look when logged
    def __repr__(self):
        return (
            f"**Player** "
            f"player_id: {self.player_id} "
            f"name: {self.name} "
            f"position: {self.position} "
            f"**Player** "
        )

class Season(db.Model):
    """
    Season Flask-SQLAlchemy Model
    Represents objects contained in the seasons table
    """
    __tablename__ = "seasons"
    year = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"**Season** " f"year: {self.year} " f"**Season** "