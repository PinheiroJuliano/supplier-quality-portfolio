import os
from sqlalchemy import create_engine

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Se estiver no Render, usa /tmp
if os.getenv("RENDER"):
    DATABASE_PATH = "/tmp/suppliers.db"
else:
    DATABASE_PATH = os.path.join(BASE_DIR, "suppliers.db")

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
