import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

def link_bank_account(account_id):
   
    load_dotenv()

    api_key = os.getenv("ALPACA_API_KEY")
    api_secret = os.getenv("ALPACA_API_SECRET")
    base_url = os.getenv("ALPACA_BROKER_URL", "https://broker-api.sandbox.alpaca.markets")

    url = f"{base_url}/v1/accounts/{account_id}/ach_relationships"

 
    payload = {
        # "bank_account_type": "CHECKING",
        # "account_owner_name": "John Doe",
        # "bank_account_number": "123456789",
        # "bank_routing_number": "021000021"
        
  "account_owner_name": "Pranjal Chaubey",
  "bank_account_type": "CHECKING",
  "bank_account_number": "32131231abc",
  "bank_routing_number": "123103716",
  "nickname": "Bank of America Checking"
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
        response_json = response.json()
        print("Full Response JSON:", response_json)  
        
        
        relationship_id = response_json.get("id")
        if relationship_id:
            print(f"Successfully linked bank account! Relationship ID: {relationship_id}")
            return relationship_id
        else:
            print("Bank account linked, but no relationship_id found.")
            return None

    except Exception:
        print("Response Text:", response.text)
        return None

if __name__ == "__main__":
    
    account_id = "4f11d94c-5963-49bb-96df-3848c11280c6"
    relationship_id = link_bank_account(account_id)

    if relationship_id:
        print(f"Use this relationship_id for transfers: {relationship_id}")
    else:
        print("Bank account linking failed.")
