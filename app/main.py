from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
return {"message": "Hello World 3DS2ON !!!"}
