
from models import db, User

#create database and tables
db.create_all()

db.session.add(Users("kim", 'kim@kim.kimkim', 'hallo'))

db.session.commit()
