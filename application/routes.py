from application import app, db
from flask import request, jsonify
from application.models import BG3Character

def format_character(character):
    return {
        "name": character.name,
        "race": character.race,
        "game_class": character.game_class,
        "background": character.background,        
    }

@app.route("/")
def hello_world():
    return jsonify({
        "title" : "Baldur's Gate 3 Companion Characters API",
        "recommendation": "Go to http://localhost:5000/characters",
    }), 200

@app.route("/characters", methods=["POST"])
def create_character():
    data = request.json
    character = BG3Character(data['name'], data['race'], data['game_class'], data['background'])
    db.session.add(character)
    db.session.commit()
    return jsonify(id=character.id, name=character.name, race=character.race, game_class=character.game_class, background=character.background)


@app.route("/characters", methods=['GET'])
def get_characters():
    characters = BG3Character.query.all()
    character_list = []
    for character in characters:
        character_list.append(format_character(character))
    return character_list


@app.route('/characters/<id>')
def get_character(id):
    character = BG3Character.query.filter_by(id=id).first()
    return jsonify(id=character.id, name=character.name, race=character.race, game_class=character.game_class, background=character.background)


@app.route("/characters/<id>", methods=['DELETE'])
def delete_character(id):
    character = BG3Character.query.filter_by(id=id).first()
    db.session.delete(character)
    db.session.commit()
    return f"Character deleted {id}"


@app.route("/characters/<id>", methods=["PATCH"])
def update_character(id):
    character = BG3Character.query.filter_by(id=id)
    data = request.json
    character.update(dict(name=data["name"], race=data["race"], game_class=data["game_class"], background=data['background']))
    db.session.commit()
    updatedCharacter = character.first()
    return jsonify(id=updatedCharacter.id, name=updatedCharacter.name, race=updatedCharacter.race, game_class=updatedCharacter.game_class, background=character.background)