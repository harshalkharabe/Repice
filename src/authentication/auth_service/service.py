import uuid
import pandas
from src.utils.logs import CustomLogger
from src.authentication.auth_models.model import User

# Create an instance of CustomLogger with desired configuration
logger_instance = CustomLogger(log_level='DEBUG', log_file_name='authentication.log', log_path='logs')

# Get the logger from the instance
logger = logger_instance.get_logger()


data = pandas.read_csv("src/authentication/user_data.csv")
users = data.to_dict(orient="records")

class UserManagement:
    def register_user(user,db):
        try:
            user.id = uuid.uuid4()
            dic = user.__dict__
            user_data = User(**dic)
            db.add(user_data)
            db.commit()
            db.refresh(user_data)
            return user_data

        except Exception as e:
            logger.error(f"Error : {str(e)}")
            return str(e)
    
    def get_all_users(db):
        try:
            result = db.query(User).all()
            return result
        except Exception as e:
            logger.error(f"Error : {str(e)}")
            return e
        
    def get_user_by_id(user_id,db):
        try:
            result = db.query(User).filter(User.id==user_id).first()
            return result
        except Exception as e:
            return e