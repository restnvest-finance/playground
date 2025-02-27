import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

def transfer_funds(account_id, amount, relationship_id):
    load_dotenv()

    api_key = os.getenv("ALPACA_API_KEY")
    api_secret = os.getenv("ALPACA_API_SECRET")
    base_url = os.getenv("ALPACA_BROKER_URL", "https://broker-api.sandbox.alpaca.markets")

    url = f"{base_url}/v1/accounts/{account_id}/transfers"

    payload = {
        "transfer_type": "ach",
        "direction": "INCOMING",
        "timing": "immediate",
        "amount": str(amount),
        "relationship_id": relationship_id  # Include this!
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers,
        auth=HTTPBasicAuth(api_key, api_secret)
    )

    print("Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except Exception:
        print("Response Text:", response.text)

if __name__ == "__main__":
    account_id = "4f11d94c-5963-49bb-96df-3848c11280c6"
    transfer_amount = 100.00

    # Get relationship_id from your bank linking function
    relationship_id = "11964109-5aca-4d7b-a4ac-add9a45a4e53"

    if relationship_id:
        transfer_funds(account_id, transfer_amount, relationship_id)
    else:
        print("No valid relationship_id found. Please link a bank account first.")
