from sqlalchemy.orm import session
from schema import UserCreate
from user import User

class UserRepository:
    def create_user(self,db:session,user_payload:User):
        db.add(user_payload)
        db.commit()

    def get_user_by_id(self,db:session,id:int):
        db_user=db.query(User).filter(User.id==id).first()
        return db_user

    def get_all_user(self,db:session):
        db_users=db.query(User).all()
        return db_users


    def delete_by_email(self,db:session,email:str):
        db_user=db.query(User).filter(User.email==email).first()
        if db_user:
            db.delete(db_user)
            db.commit()



 