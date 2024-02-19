from fastapi import FastAPI

app = FastAPI()

@app.get("/getcode")
async def root():
    return {"message": "Softdev Inpractice gametuatueng"}

@app.get("/plus/{num1}/{num2}")
async def root(num1: int, num2: int):
    result = num1 + num2
    return {"result": result}