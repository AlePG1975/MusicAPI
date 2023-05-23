from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return "Hola!, que quieres escuchar?"

@app.get("/MusicAPI/{num}")
def musicapi(num):
    return num

@app.get("/Conversor_CaF/{C}")
def conversorCaF(C):
   TF=C*(9/5) + 32
return f"La temperatura es de:{TF]grados Fahrenheit"
    
