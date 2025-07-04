from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(20),nullable=False)
    email=db.Column(db.String(),nullable=False,unique=True)
    password=db.Column(db.String(20),nullable=False)
    
    
class Category(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(20),nullable=False)
    
class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(20),nullable=False)
    price=db.Column(db.Float,nullable=False)
    quantity=db.Column(db.Integer,nullable=False)
    unit=db.Column(db.Integer,nullable=False)
    category_id=db.Column(db.Integer,db.ForeignKey("category.id"),nullable=False)
        
    
    
    