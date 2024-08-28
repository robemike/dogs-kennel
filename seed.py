from models import db, Dog
from app import app

with app.app_context():
    print('Deleting dog database...')
    Dog.query.delete()

    print('Creating new dog database...')
    yuki = Dog(name='yuki', species='German shepherd')
    spikes = Dog(name='spikes', species='Rottweiler')
    zuki = Dog(name='zuki', species='American Pitbull')

    print('Adding dogs to transaction...')
    db.session.add_all([yuki, zuki, spikes])

    print('Committing transaction...')
    db.session.commit()

    print('All dogs have been added to the database.')
