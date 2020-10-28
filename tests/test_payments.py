import json
import requests


def test_process_payments_ok():
    with open('tests/sample_input.json') as f:
        test_data = json.load(f)

    r = requests.post('http://127.0.0.1:8000/payments/', data=json.dumps(test_data))

    assert r.status_code == 200

def test_process_payments_expired():
    with open('tests/expiredcard_input.json') as f:
        test_data = json.load(f)

    r = requests.post('http://127.0.0.1:8000/payments/', data=json.dumps(test_data))

    assert r.status_code == 400

def test_process_payments_negative():
    with open('tests/negative_input.json') as f:
        test_data = json.load(f)

    r = requests.post('http://127.0.0.1:8000/payments/', data=json.dumps(test_data))

    assert r.status_code == 400

def test_process_payments_invalid_card():
    with open('tests/invalidcard_input.json') as f:
        test_data = json.load(f)

    r = requests.post('http://127.0.0.1:8000/payments/', data=json.dumps(test_data))

    assert r.status_code == 400