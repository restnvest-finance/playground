import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

def create_account():

    load_dotenv()

   
    api_key = os.getenv("ALPACA_API_KEY")
    api_secret = os.getenv("ALPACA_API_SECRET")
    base_url = os.getenv("ALPACA_BROKER_URL", "https://broker-api.sandbox.alpaca.markets")

    url = f"{base_url}/v1/accounts"
    
   
    payload = {
        "identity": {
            "given_name": "John",
            "middle_name": "A",
            "family_name": "Doe",
            "date_of_birth": "1980-01-01",  
            "tax_id": "132333458",
            "tax_id_type": "USA_SSN",
            "country_of_citizenship": "USA",
            "country_of_birth": "USA",
            "country_of_tax_residence": "USA",
            "funding_source": ["employment_income", "savings"],
            "phone_number": "5551234567"
        },
        "contact": {
            "email_address": "john.doe@example.com",
            "phone_number": "5551234567",
            "street_address": [
                "123 Main Street",
                "Apt 1"
            ],
            "city": "New York",
            "state": "NY",
            "postal_code": "10001",
            "country": "USA"
        },
        "disclosures": {
            "is_control_person": False,
            "is_affiliated_exchange_or_finra": False,
            "is_politically_exposed": False,
            "immediate_family_exposed": False
        },
        "agreements": [
            {
                "agreement": "account_agreement",
                "signed_at": "2023-01-01T00:00:00Z",
                "ip_address": "192.168.0.1"
            },
            {
                "agreement": "customer_agreement",
                "signed_at": "2023-01-01T00:00:00Z",
                "ip_address": "192.168.0.1"
            },
            {
                "agreement": "margin_agreement",
                "signed_at": "2023-01-01T00:00:00Z",
                "ip_address": "192.168.0.1"
            },
            
        ]
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
    create_account()
