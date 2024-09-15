from datetime import datetime, timedelta
import uuid
from jose import JWTError, jwt
from fastapi import Depends, APIRouter, HTTPException, Path
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from src.authentication.auth_dao.dao import UserDAO
from src.db_session import get_db
from src.authentication.auth_models.model import User_v2,User_Login
from src.authentication.auth_service.service import UserManagement
from src.utils.logs import CustomLogger
from sqlalchemy.orm import Session

SECRET_KEY = "011932153fd276ab814787646c6495032f6d0974ac31c508cfdc7918f6b03126"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 50


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token/")

# Helper function to verify and decode the JWT token
# Corrected token creation

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=403, detail="Could not validate credentials")

# Dependency to get current user
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    username = verify_token(token)
    user = UserDAO.find_user_by_username(username, db)
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    return user

logger_instance = CustomLogger(log_level='DEBUG', log_file_name='authentication.log', log_path='logs')


logger = logger_instance.get_logger()

class UserManagementApi:

    router = APIRouter()

    @router.post("/token/")
    async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db:str=Depends(get_db)):
        try:
            access_token= UserManagement.login_for_access_token(form_data,db)
            logger.info(f'User {form_data.username} logged in.')
            return access_token
        except Exception as e:
            logger.error(f"Error in login_for_access_token {str(e)}")
            raise HTTPException(status_code=400, detail="Incorrect username or password")

    
    @router.post("/register/")
    async def register(user:User_v2,db:Session=Depends(get_db)):
        try:
            result = UserManagement.register_user(user,db)
            return result
        except Exception as e:
            logger.error(f"Error while user registration {str(e)}")
            return e
        
    @router.get("/user/{user_id}/")
    async def get_user_by_id(user_id:uuid.UUID=Path(),current_user:str=Depends(get_current_user),db:Session=Depends(get_db)):
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