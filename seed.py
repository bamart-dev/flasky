from app import create_app, db
from app.models.cat import Cat

my_app = create_app()
with my_app.app_context():
    db.session.add(Cat(name="Aang", color="orange", personality="a schmoo"))
    db.session.add(Cat(name="Yue", color="black", personality="Moon Queen"))
    db.session.add(Cat(
        name="Olenna", color="light brown", personality="Fickle"))
    db.session.add(Cat(name="Luna", color="ash", personality="Tomato Queen"))
    db.session.add(Cat(name="Adella", color="grey", personality="aloof"))
    db.session.add(Cat(name="Stella", color="grey", personality="skittish"))
    db.session.commit()
