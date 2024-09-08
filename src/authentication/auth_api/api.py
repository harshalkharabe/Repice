import uuid
from fastapi import Depends, APIRouter, HTTPException, Path
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from src.db_session import get_db
from src.authentication.auth_models.model import User_v2,User_Login
from src.authentication.auth_service.service import UserManagement
from src.utils.logs import CustomLogger
from sqlalchemy.orm import Session

SECRET_KEY = "011932153fd276ab814787646c6495032f6d0974ac31c508cfdc7918f6b03126"
ALOGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 50


logger_instance = CustomLogger(log_level='DEBUG', log_file_name='authentication.log', log_path='logs')


logger = logger_instance.get_logger()

class UserManagementApi:

    router = APIRouter()
    
    @router.post("/register/")
    async def register(user:User_v2,db:Session=Depends(get_db)):
        try:
            result = UserManagement.register_user(user,db)
            return result
        except Exception as e:
            logger.error(f"Error while user registration {str(e)}")
            return e
        
    @router.get("/user/{user_id}/")
    async def get_user_by_id(user_id:uuid.UUID=Path(),db:Session=Depends(get_db)):
        try:
            result = UserManagement.get_user_by_id(user_id,db)
            return result
        except Exception as e:
            logger.error(f"Error while user registration {str(e)}")
            return e
        
    @router.post('/login/')
    async def login(user:User_Login,db:str=Depends(get_db)):
        try:
            result = UserManagement.login(user,db)
            return result
        except Exception as e:
            logger.error(f"Login Error : {str(e)}")
            return str(e)