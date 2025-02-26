import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

def get_linked_banks(account_id):
   
    load_dotenv()

    
    api_key = os.getenv("ALPACA_API_KEY")
    api_secret = os.getenv("ALPACA_API_SECRET")
    base_url = os.getenv("ALPACA_BROKER_URL", "https://broker-api.sandbox.alpaca.markets")

    
    url = f"{base_url}/v1/accounts/{account_id}/recipient_banks"

    
    response = requests.get(url, auth=HTTPBasicAuth(api_key, api_secret))

   
    print("Status Code:", response.status_code)
    try:
        response_data = response.json()
        print("Response JSON:", response_data)

        
        if isinstance(response_data, list) and len(response_data) > 0:
            for bank in response_data:
                print(f"Bank Name: {bank.get('bank_name')}, Relationship ID: {bank.get('id')}")
            return response_data[0].get('id')  
        else:
            print("No linked banks found.")
            return None
    except Exception:
        print("Response Text:", response.text)
        return None

if __name__ == "__main__":
    
    account_id = "56eb1cff-a756-42f7-bae5-46d51aa12649"
    relationship_id = get_linked_banks(account_id)

    if relationship_id:
        print(f"Your relationship_id: {relationship_id}")
    else:
        print("No relationship_id found. Link a bank account first.")
