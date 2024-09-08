from src.authentication.auth_models.model import User


class UserDAO:    

    @staticmethod
    def get_user_by_id(user_id,db):
        result = db.query(User).filter(User.id==user_id).first()
        return result

    @staticmethod
    def get_user_by_username(user,db):
        query = db.query(User).filter(User.username==user.username,User.password==user.password).first()
        return query

    @staticmethod
    def update_user_login_status(username: str, is_logged_in: bool,db):
        try:
            db.query(User).filter(User.username == username).update({User.is_logged_in: is_logged_in})
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            raise e