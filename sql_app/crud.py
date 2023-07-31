from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_firstname(db: Session, first_name: str):
#     return db.query(models.User).filter(models.User.first_name == first_name).first()

def get_user_by_firstname(db: Session, first_name: str):
    tag = first_name
    search = "{}%".format(tag)
    return db.query(models.User).filter(models.User.first_name.like(search)).all()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email, 
        age=user.age, 
        gender=user.gender,
        phone=user.phone,
        birth_date=user.birth_date
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user






