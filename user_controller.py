
from fastapi import APIRouter,Depends
from schema import UserCreate
from user import User
from database import get_db
from service import UserService
from sqlalchemy.orm import Session


router=APIRouter(
    prefix="/user"
)

@router.post("/create")

def create_user(payload:UserCreate,db:Session=Depends(get_db)):
    service=UserService()
    service.create_user(db,payload)


@router.get("/list")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/{email}")

def get_user_by_email(email:str,db:Session=Depends(get_db)):
    service=UserService()
    return service.get_user_by_email(db,email)

@router.delete("/{email}")
def delete_user_by_email(email:str,db:Session=Depends(get_db)):
    service=UserService()
    return service.delete_by_email(db,email)
