from fastapi import FastAPI
import pandas as pd
from app.database import engine
from app import etl

app = FastAPI(title="Supplier Quality API")

@app.on_event("startup")
def startup_event():
    etl.run()

@app.get("/")
def root():
    return {"service": "Supplier Quality API", "status": "running"}

@app.get("/suppliers/kpis")
def get_kpis():
    df = pd.read_sql("suppliers_kpis", engine)
    return df.to_dict(orient="records")
