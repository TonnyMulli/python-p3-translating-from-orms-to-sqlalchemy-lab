from models import Dog

def create_table(base, engine):
    base.metadata.create_all(bind=engine)
def save(session, dog):
    session.add(dog)
    session.commit()
def get_all(session):
    dogs = session.query(Dog).all()
    return dogs
def find_by_name(session, name):
    query = session.query(Dog).filter(Dog.name == name)
    return query.first()
def find_by_id(session, id):
    query = session.query(Dog).filter(Dog.id == id)
    return query.first()
def find_by_name_and_breed(session, name, breed):
    query = session.query(Dog).filter(Dog.name == name, Dog.breed == breed)
    return query.first()
def update_breed(session, dog, breed):
    session.query(Dog).filter(Dog.id == dog.id).update({"breed": breed})
    session.commit()
