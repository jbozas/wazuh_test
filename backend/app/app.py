from app import app
from app.models import *

print('Creating the app')
print('Initializating db.')
db.create_all(app=app)

if __name__=='__main__':
    print('App running.')
    app.run()