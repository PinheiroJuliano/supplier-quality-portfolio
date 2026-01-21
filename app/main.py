from fastapi import FastAPI

app = FastAPI(title="Supplier Quality API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/suppliers/kpis")
def get_kpis():
    return [{"supplier": "Test", "score": 95}]

@app.get("/")
def root():
    return {
        "service": "Supplier Quality API",
        "status": "running"
    }
