from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

@app.get("/")
def index():
    return "Hola!, que quieres escuchar?"

@app.get("/MusicAPI/{num}")
def musicapi(num):
    music={
        "1":"Dealer",
        "2":"Say Yes To Have",
        "3":"Radio",
        "4":"Art Deco",
        
    }
    return (musicapi[num])

@app.get("/Conversor_CaF/{C}")
def conversorCaF(C):
    try:
          C=float(c)
          TF=C*(9/5) + 32
          return f"La temperatura es de:{TF}grados Fahrenheit"
    exept:
            return "Entrada invalida"
@app.get("/RevisarEdad/{E1}/{E2}")
def revisar_edades(E1,E2):
    E1=int(E1)
    E2=int(E2)
    if E1>E2+30:
        return "Podrias ser su Abuelo"
    elif E1>E2+15:
        return "Podrias ser su padre"
    elif E1>E2:
        return "Eres mayor"
    if E1>E2+30:
        return "Podria ser su Abuelo"
    elif E1>E2+15:
        return "Podria ser su padre"
    elif E1>E2:
        return "Eres mayor que tu"
    else:
    return "Tiene la misma edad"

