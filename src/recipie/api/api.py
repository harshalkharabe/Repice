from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.recipie.services.service import RecipeService
from src.db_session import get_db
from src.authentication.auth_api.api import get_current_user
from src.recipie.model.model import RecipeBase
from src.utils.logs import CustomLogger



logger_instance = CustomLogger(log_level='DEBUG', log_file_name='recipe.log', log_path='logs')
logger = logger_instance.get_logger()

class RecipeAPI:
    router = APIRouter()

    def __init__(self) -> None:
        pass
    
    @router.post("/recipes/")
    def create_recipe(recipe: RecipeBase, current_user: str = Depends(get_current_user), db: Session = Depends(get_db)):
        try:
            print("H")
            result =  RecipeService.create(recipe,current_user,db)
            return result
        except Exception as e :
            logger.error(f"Error : {str(e)}")
            return str(e)