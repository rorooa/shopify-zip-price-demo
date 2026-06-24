from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

prices = {
    "75028": 1499,
    "10001": 1699,
    "90210": 1799
}

@app.get("/")
def home():
    return {"message": "API Running"}

@app.get("/price")
def get_price(zipcode: str):
    return {
        "zipcode": zipcode,
        "price": prices.get(zipcode, 1599)
    }