from routes import db
from models import User

#create database and tables
db.create_all()

db.session.add(Users("kim", 'kim@kim.com', 'hallo'))

db.session.commit()
