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
    try:
          C=float(c)
          TF=C*(9/5) + 32
          return f"La temperatura es de:{TF}grados Fahrenheit"
    exept:
            return "Entrada invalida"
