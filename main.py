from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return "Hola!, que quieres escuchar?"

@app.get("/MusicAPI/{num}")
def musicapi(num):
    return num
