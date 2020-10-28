import random

class PayProcessors(object):

    SUCCESS_MESSAGE = {"message" : "Your payment was successfully processed."}
    FAIL_MESSAGE = {"message" : "Your payment was NOT processed."}

    @classmethod
    def process_cheap(cls):
        if is_cheap_gateway_available():
            return cls.SUCCESS_MESSAGE
        else:
            return cls.FAIL_MESSAGE

    @classmethod
    def process_expensive(cls):
        if is_expensive_gateway_available():
            return cls.SUCCESS_MESSAGE
        else:
            cls.process_cheap()

    @classmethod
    def process_premium(cls):
        attempts = 0
        while attempts <= 3:
            if is_premium_gateway_available():
                return cls.SUCCESS_MESSAGE
            else:
                attempts += 1

        return cls.FAIL_MESSAGE


def is_cheap_gateway_available():
    return random.random() > 0.5

def is_expensive_gateway_available():
    return random.random() > 0.3

def is_premium_gateway_available():
    return random.random() > 0.2