import create_account
import link_bank_account
import transfer_funds

def main():

    print("Creating account...")
    create_account.create_account()
    account_id = "4f11d94c-5963-49bb-96df-3848c11280c6"  
    print("\nLinking bank account...")
    relationship_id = link_bank_account.link_bank_account(account_id)
    if not relationship_id:
        print("Bank account linking failed. Exiting...")
        return

    print("\nTransferring funds...")
    transfer_amount = 100.00  
    transfer_funds.transfer_funds(account_id, transfer_amount, relationship_id)

if __name__ == "__main__":
    main()
