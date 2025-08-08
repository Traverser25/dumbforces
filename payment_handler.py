import  razorpay 


import os
import requests
from dotenv import load_dotenv
import logging

load_dotenv()

# Setup logging
logging.basicConfig(filename='main.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RazorpayPayout:
    def __init__(self):
        self.api_key = os.getenv("RAZORPAY_KEY_ID")
        self.api_secret = os.getenv("RAZORPAY_KEY_SECRET")
        self.account_number = os.getenv("RAZORPAY_ACCOUNT_NUMBER")  # RazorpayX virtual account number
        self.base_url = "https://api.razorpay.com/v1/payouts"

        if not all([self.api_key, self.api_secret, self.account_number]):
            raise ValueError("Missing Razorpay credentials in .env file")

    def send_money(self, name, ifsc, acc_no, email, phone, amount_rupees, purpose="payout"):
        """Send money to a bank account via RazorpayX (for meme testing)"""
        amount_paise = int(amount_rupees * 100)

        payload = {
            "account_number": self.account_number,
            "fund_account": {
                "account_type": "bank_account",
                "bank_account": {
                    "name": name,
                    "ifsc": ifsc,
                    "account_number": acc_no
                },
                "contact": {
                    "name": name,
                    "type": "employee",
                    "email": email,
                    "contact": phone
                }
            },
            "amount": amount_paise,
            "currency": "INR",
            "mode": "IMPS",
            "purpose": purpose,
            "queue_if_low_balance": True
        }

        try:
            logging.info(f"Initiating payout of ₹{amount_rupees} to {name}")
            response = requests.post(
                self.base_url,
                auth=(self.api_key, self.api_secret),
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            result = response.json()

            if response.status_code == 200 or response.status_code == 201:
                logging.info(f"Payout success: {result.get('id')}")
            else:
                logging.error(f" Payout failed: {result}")
            return result

        except Exception as e:
            logging.error(f"Exception during payout: {e}")
            return {"error": str(e)}
