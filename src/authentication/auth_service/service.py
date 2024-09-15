from datetime import timedelta
import uuid
from fastapi import HTTPException
from jose import JWTError, jwt
import pandas
from datetime import datetime, timedelta, timezone
from src.utils.logs import CustomLogger
from src.authentication.auth_models.model import User
from src.authentication.auth_dao.dao import UserDAO

# Create an instance of CustomLogger with desired configuration
logger_instance = CustomLogger(log_level='DEBUG', log_file_name='authentication.log', log_path='logs')

# Get the logger from the instance
logger = logger_instance.get_logger()

SECRET_KEY = "011932153fd276ab814787646c6495032f6d0974ac31c508cfdc7918f6b03126"
ALOGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta = None):
    try:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALOGORITHM)
        return encoded_jwt
    except Exception as e:
            raise HTTPException(status_code=400, detail="Error in create_access_token")


class UserManagement:

    @staticmethod
    def login_for_access_token(form_data,db):
        find_user_by_username=UserDAO.find_user_by_username(form_data.username,db)
        if find_user_by_username:
            if find_user_by_username.password == form_data.password:
                #change user login status to yes
                status = UserDAO.update_user_login_status(form_data.username,True,db)
                # Generate a JWT token
                access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
                access_token = create_access_token(
                    data={
                        "sub": form_data.username,
                        "user_id":str(find_user_by_username.id),
                    },
                    expires_delta=access_token_expires)
                
                response_data = {
                "message":f"{find_user_by_username.username} logged in successfully",
                "access_token": access_token,
                "token_type": "bearer",
                "user_id": f"{find_user_by_username.id}"
                 }
                return response_data
            else:
                raise HTTPException(status_code=400, detail="Incorrect password")
        else:
            raise HTTPException(status_code=400, detail="User not registered")

    def register_user(user,db):
        try:
            find_user_by_email = db.query(User).filter(User.email==user.email).first()
            if find_user_by_email:
                return "User already registered"
            else:
                find_user_by_username = db.query(User).filter(User.username==user.username).first()
                if find_user_by_username:
                    return "Username already used"
                else:    
                    user.id = uuid.uuid4()
                    dic = user.__dict__
                    user_data = User(**dic)
                    db.add(user_data)
                    db.commit()
                    db.refresh(user_data)
                    logger.info(f"Register user successfully {dic}")
                    return user_data

        except Exception as e:
            logger.error(f"Error : {str(e)}")
            return str(e)
    
    def get_user_by_id(user_id,db):
        try:
            result = UserDAO.get_user_by_id(user_id,db)
            return result
        except Exception as e:
            return e
    
    def login(user,db):
        try:
            user_data = UserDAO.get_user_by_username_password(user,db)
            if user_data:
                UserDAO.update_user_login_status(user.username,True,db)
                logger.info(f"{user_data.username} is logging successfully")
                return {"message":"User Login Successfully"}
            else:
                return "User dose not exist"
        except Exception as e:
            logger.error(f"Error : {e}")
            return str(e)