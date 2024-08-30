import uuid
import pandas
from src.utils.logs import CustomLogger

# Create an instance of CustomLogger with desired configuration
logger_instance = CustomLogger(log_level='DEBUG', log_file_name='authentication.log', log_path='logs')

# Get the logger from the instance
logger = logger_instance.get_logger()


data = pandas.read_csv("src/authentication/user_data.csv")
users = data.to_dict(orient="records")

class UserManagement:
    def register_user(user):
        try:
            user.id = uuid.uuid4()
            new_user = user.model_dump()
            users.append(new_user)
            # print(new_book)
            data = pandas.DataFrame(users)
            data.to_csv("src/authentication/user_data.csv", index=False)
            logger.info(f"User Register Successfully {user}")
            return new_user
        except Exception as e:
            logger.error(f"Error : {str(e)}")
            return str(e)
    
    def get_all_users():
        try:
            if len(users) == 0:
                logger.info("File is empty!!")
                return "Data not found!!"
            else:
                logger.info(f"Get all register users")
                return users
        except Exception as e:
            return e
        
    def get_user_by_id(user_id):
        try:
            for user in users:
                user_id = str(user_id)
                if user_id==user['id']:
                    return user
                break
            else:
                logger.info(f"User not register")
                return "User not found"
        except Exception as e:
            return e