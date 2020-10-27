from fastapi import FastAPI
from base_models import PaymentInfo

app = FastAPI()

@app.post("/payments/")
async def process_payments(payment_info: PaymentInfo):

    result = []
    
    return result