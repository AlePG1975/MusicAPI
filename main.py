from fastapi import FastAPI

app=FastAPI()
@app.get("/")
def index():
    return "Hi Bicht, que quieres escuchar?"
