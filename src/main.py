from fastapi import FastAPI, Request
from src.authentication.auth_api.api import UserManagementApi
from src.recipie.api.api import RecipeAPI
from src.utils.logs import CustomLogger


logger_instance = CustomLogger(log_level='DEBUG', log_file_name='main.log', log_path='logs')
logger = logger_instance.get_logger()

app = FastAPI(
    title="Recipe Project API",
    description="These are the API's for Harshal's Project",
    # openapi_url="/auth/openapi.json",
    docs_url="/harshal/docs", redoc_url=None
)


# UserManagementApi = api.UserManagementApi()
app.include_router(UserManagementApi.router, tags=["User Authentication"])
app.include_router(RecipeAPI.router, tags=["Recipes"])