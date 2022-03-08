from fastapi import FastAPI
from pydantic import BaseModel, Field
from utils.nasdaq import symbol_exists_on_nasdaq
app = FastAPI()


class Share(BaseModel):
    qty: int = Field(..., gt=0, description="The quantity must be greater than zero")
    symbol:str


@app.post("/shares/{transaction_type}",status_code=200)
async def transaction(transaction_type:str, share: Share):
    is_valid_symbol = symbol_exists_on_nasdaq(share.symbol)
    if (is_valid_symbol):
        data =""
        if transaction_type == "buy":
            data="Bought"
        elif transaction_type == "sell":
            data = "Sold"
        else:
            pass
        return {"error": False, "data": data, "message": "Found symbol", "statusCode":200}
    else:
        return {"error": True, "message": "Not found symbol", "statusCode":404}