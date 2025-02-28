import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

def load_env():
    load_dotenv()
    return {
        "api_key": os.getenv("ALPACA_API_KEY"),
        "api_secret": os.getenv("ALPACA_API_SECRET"),
        "base_url": os.getenv("ALPACA_BROKER_URL", "https://broker-api.sandbox.alpaca.markets")
    }

def transfer_funds(account_id, amount, relationship_id):
    env = load_env()
    
    url = f"{env['base_url']}/v1/accounts/{account_id}/transfers"
    payload = {
        "transfer_type": "ach",
        "direction": "INCOMING",
        "timing": "immediate",
        "amount": str(amount),
        "relationship_id": relationship_id
    }
    headers = {"accept": "application/json", "content-type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers, auth=HTTPBasicAuth(env['api_key'], env['api_secret']))
    print("Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except Exception:
        print("Response Text:", response.text)

def create_account():
    env = load_env()
    
    url = f"{env['base_url']}/v1/accounts"
    payload = {
        "identity": {
            "given_name": "Pranjal",
            "middle_name": "A",
            "family_name": "Chaubey",
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
            "email_address": "pranjalchaubey001@gmail.com",
            "phone_number": "5551234567",
            "street_address": ["123 Main Street", "Apt 1"],
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
            {"agreement": "account_agreement", "signed_at": "2023-01-01T00:00:00Z", "ip_address": "192.168.0.1"},
            {"agreement": "customer_agreement", "signed_at": "2023-01-01T00:00:00Z", "ip_address": "192.168.0.1"},
            {"agreement": "margin_agreement", "signed_at": "2023-01-01T00:00:00Z", "ip_address": "192.168.0.1"}
        ]
    }
    headers = {"accept": "application/json", "content-type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers, auth=HTTPBasicAuth(env['api_key'], env['api_secret']))
    print("Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except Exception:
        print("Response Text:", response.text)

def link_bank_account(account_id):
    env = load_env()
    
    url = f"{env['base_url']}/v1/accounts/{account_id}/ach_relationships"
    payload = {
        "account_owner_name": "Pranjal Chaubey",
        "bank_account_type": "CHECKING",
        "bank_account_number": "32131231abc",
        "bank_routing_number": "123103716",
        "nickname": "Bank of America Checking"
    }
    headers = {"accept": "application/json", "content-type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers, auth=HTTPBasicAuth(env['api_key'], env['api_secret']))
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
    transfer_amount = 100.00
    
    create_account()
    relationship_id = link_bank_account(account_id)
    
    if relationship_id:
        transfer_funds(account_id, transfer_amount, relationship_id)
    else:
        print("Bank account linking failed.")
