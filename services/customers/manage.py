#services/customers/manage.py

from flask.cli import FlaskGroup
from project import app, db
cli = FlaskGroup(app)


if __name__== '__main__':
    db.create_all()
    cli()
