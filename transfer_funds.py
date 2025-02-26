import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

def transfer_funds(account_id, amount):
    
    load_dotenv()

    
    api_key = os.getenv("ALPACA_API_KEY")
    api_secret = os.getenv("ALPACA_API_SECRET")
    base_url = os.getenv("ALPACA_BROKER_URL", "https://broker-api.sandbox.alpaca.markets")

   
    url = f"{base_url}/v1/accounts/{account_id}/transfers"

 
    payload = {
        "transfer_type": "ach",      
        "direction": "INCOMING",     
        "timing": "immediate",       
        "amount": str(amount)        
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
    
    account_id = "56eb1cff-a756-42f7-bae5-46d51aa12649"
    transfer_amount = 100.00  
    transfer_funds(account_id, transfer_amount)
