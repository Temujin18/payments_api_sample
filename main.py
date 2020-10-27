import uvicorn
from fastapi import FastAPI
from base_models import PaymentInfo
from pay_processors import PayProcessors

app = FastAPI()

@app.post("/payments/")
async def process_payments(payment_info: PaymentInfo):

    if payment_info.amount <= 20:
        return PayProcessors.process_cheap()
    elif payment_info.amount <= 500:
        return PayProcessors.process_expensive()
    else:
        return PayProcessors.process_premium()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)