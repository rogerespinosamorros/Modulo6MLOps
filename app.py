from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return "Hola, CodeSpace"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)