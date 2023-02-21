# Here, we are querying a database


from sqlalchemy.orm import Session

from . import models, schemas
import bcrypt


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    # This will get all users in our db
    return db.query(models.User).offset(skip).limit(limit).all()


# We are passing in a user create object inside of schemas.py
def create_user(db: Session, user: schemas.UserCreate):

    hashed_password = bcrypt.hashpw(
        user.password.encode('utf-8'), bcrypt.gensalt())
    # We are calling the User model in our database. (inside of models.py)
    db_user = models.User(
        email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()  # We are saving this instance to the database
    db.refresh(db_user)  # This will add the id to the db user instance


def check_username_password(db: Session, user: schemas.UserCreate):
    db_user_info: models.UserInfo = get_users(db, username=user.username)
    return bcrypt.checkpw(user.password.encode('utf-8'), db_user_info.password.encode('utf-8'))


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


# grabbing the user id and associating it with the new item
def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item





