from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from state import window
from utils import fetch_numbers

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Average Calculator API"}

@app.get("/numbers/{numberid}")
async def get_numbers(numberid: str):
    if numberid not in ['p', 'f', 'e', 'r']:
        raise HTTPException(status_code=400, detail="Invalid number ID")

    prev_window = list(window)
    new_numbers = await fetch_numbers(numberid)

    for num in new_numbers:
        if num not in window:
            window.append(num)

    current_window = list(window)
    avg = round(sum(current_window) / len(current_window), 2) if current_window else 0

    return JSONResponse({
        "windowPrevState": prev_window,
        "windowCurrState": current_window,
        "numbers": new_numbers,
        "avg": avg
    })
