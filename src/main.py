import requests
import os

FASTAPI_ENDPOINT = os.getenv("FASTAPI_ENDPOINT")
ENV = os.getenv("ENV")

def lambda_handler(event, context):
    if ENV == "LOCAL":
        protocol = "http"
    else:
        protocol = "https"
    response = requests.get(f"{protocol}://{FASTAPI_ENDPOINT}/health")
    return response.json()


