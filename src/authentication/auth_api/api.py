import uuid
from fastapi import Depends, APIRouter, HTTPException, Path
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from src.authentication.auth_models.model import User_v2
from src.authentication.auth_service.service import UserManagement
from src.utils.logs import CustomLogger

# Create an instance of CustomLogger with desired configuration
logger_instance = CustomLogger(log_level='DEBUG', log_file_name='authentication.log', log_path='logs')

# Get the logger from the instance
logger = logger_instance.get_logger()

class UserManagementApi:

    router = APIRouter()
    
    @router.post("/register/")
    def register(user:User_v2):
        try:
            result = UserManagement.register_user(user)
            return result
        except Exception as e:
            logger.error(f"Error while user registration {str(e)}")
            return e
        
    @router.get("/register/")
    def read_register_user():
        try:
            result = UserManagement.read_register_user()
            return result
        except Exception as e:
            logger.error(f"Error while user registration {str(e)}")
            return e
        
    @router.get("/register/{user_id}/")
    def read_register_user(user_id:uuid.UUID=Path()):
        try:
            result = UserManagement.read_register_user_by_id(user_id)
            return result
        except Exception as e:
            logger.error(f"Error while user registration {str(e)}")
            return e