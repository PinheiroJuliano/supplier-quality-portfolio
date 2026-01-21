from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd

app = FastAPI(title="Supplier Quality API")

engine = create_engine("sqlite:///data/suppliers.db")

@app.get("/suppliers/kpis")
def get_kpis():
    df = pd.read_sql("suppliers_kpis", engine)
    return df.to_dict(orient="records")

from app.etl import *

@app.on_event("startup")
def startup_event():
    pass  # ETL já executa ao importar
