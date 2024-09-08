import uuid
import pandas
from src.utils.logs import CustomLogger
from src.authentication.auth_models.model import User
from src.authentication.auth_dao.dao import UserDAO

# Create an instance of CustomLogger with desired configuration
logger_instance = CustomLogger(log_level='DEBUG', log_file_name='authentication.log', log_path='logs')

# Get the logger from the instance
logger = logger_instance.get_logger()


class UserManagement:

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
            user_data = UserDAO.get_user_by_username(user,db)
            if user_data:
                UserDAO.update_user_login_status(user.username,True,db)
                logger.info(f"{user_data.username} is logging successfully")
                return {"message":"User Login Successfully"}
            else:
                return "User dose not exist"
        except Exception as e:
            logger.error(f"Error : {e}")
            return str(e)