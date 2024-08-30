from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
#from sqlalchemy.ext.declarative import declarative_base


host = "localhost"
port = 5432
username = "postgres"
password = "harshdmt"
database = "Recipe"
schema = "public"

database_url = f"postgresql://{username}:{password}@{host}:{port}/{database}"

# SQLALCHEMY_DATABASE_URL = "postgresql://admin:admin@db/datamatter"
SQLALCHEMY_DATABASE_URL = database_url

# # Create the SQLAlchemy engine
# engine = create_engine(SQLALCHEMY_DATABASE_URL,
#     pool_size=10,
#     max_overflow=20,
#     pool_timeout=30,
#     pool_recycle=1800,
#     pool_pre_ping=True,
#     pool_use_lifo=True)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a SessionLocal class to handle database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Base.metadata.schema = "dev"


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# from sqlalchemy import inspect
# inspector = inspect(engine)
# columns = inspector.get_columns('project')
# for column in columns:
