
from models import db, User
from routes import create_app

#create database and tables
db.create_all(app = create_app())

#user = User("kim", "kim@kim.kimkim", "password")

#db.session.add(user)

#db.session.commit()
