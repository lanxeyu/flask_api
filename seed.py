from application import db
from application.models import BG3Character

db.drop_all()
print('Dropping database')
db.create_all()
print('Creating database')

print('Seeding database')
entry1 = BG3Character(name="Lae'zel", race="Githyanki", game_class="Fighter", background="Soldier")
entry2 = BG3Character(name="Shadowheart", race="Half-Elf", game_class="Cleric", background="Acolyte")
entry3 = BG3Character(name="Gale", race="Human", game_class="Wizard", background="Sage")
entry4 = BG3Character(name="Astarion", race="Elf", game_class="Rogue", background="Charlatan")
entry5 = BG3Character(name="Wyll", race="Human", game_class="Warlock", background="Folk Hero")
entry6 = BG3Character(name="Karlach", race="Tiefling", game_class="Barbarian", background="Outlander")
entry7 = BG3Character(name="Minthara", race="Drow", game_class="Paladin", background="Noble")
entry8 = BG3Character(name="Halsin", race="Elf", game_class="Druid", background="Outlander")
entry9 = BG3Character(name="Jaheira", race="Half-Elf", game_class="Druid", background="Soldier")
entry10 = BG3Character(name="Minsc", race="Human", game_class="Ranger", background="Folk Hero")

db.session.add_all([entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10])

db.session.commit()