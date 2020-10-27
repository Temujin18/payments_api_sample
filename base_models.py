from pydantic import BaseModel, Field, ValidationError, validator
from datetime import datetime
from typing import Optional
from utils import is_mod10_valid, is_expired
from fastapi import HTTPException

class PaymentInfo(BaseModel):
    credit_card_number: str
    card_holder: str
    expiration_date: datetime
    security_code: Optional[str] = Field(None, regex="^\d{3}$")
    amount: float

    @validator('credit_card_number')
    def credit_card_is_valid(cls, v):
        if not is_mod10_valid(v):
            raise HTTPException(status_code=400, detail='Credit Card Number is not valid.')
        return v

    @validator('expiration_date')
    def credit_card_is_expired(cls, v):
        if is_expired(v):
            raise HTTPException(status_code=400, detail='Credit Card is expired.')
        return v

    @validator('amount')
    def amount_is_positive(cls, v):
        try:
            amount = float(v)
        except (ValueError, TypeError):
            raise HTTPException(status_code=400, detail='Amount entered is invalid.')

        if amount < 0:
            raise HTTPException(status_code=400, detail='Amount cannot be a negative value.')

        return v
        