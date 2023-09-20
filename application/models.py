from application import db, app

app.app_context().push()

class BG3Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    race = db.Column(db.String(100), nullable=False)
    game_class = db.Column(db.String(100), nullable=False)
    background = db.Column(db.String(100), nullable=False)
    
    def __init__(self, name, race, game_class, background):
        self.name = name
        self.race = race
        self.game_class = game_class
        self.background = background
    
    def __repr__(self):
        return f"I am {self.name}, a {self.race} {self.game_class}."