
# main.py
from dotenv import load_dotenv
from cf_handler import CodeforcesChecker
from disrespect_handler import DisrespectHandler
from insta_handler import InstaHandler
from payment_handler import RazorpayPayout
import logging
import os

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, "main.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



def main():
    load_dotenv()

    cf = CodeforcesChecker()
    solved = cf.get_accepted_today()
    print(f"Problems solved today: {solved}")

    if solved < 2:
        print("Punishment routine initiated.")

        # Generate roast
        dh = DisrespectHandler()
        roasts = dh.generate_roasts(
            target="my lazy self who skips coding",
            tone="extra dramatic and flamboyant",
            count=1
        )

        roast_text = roasts[0] if roasts else "No roast generated."
        print(f"Generated self diss : {roast_text}")

        # Post roast to Instagram
        try:
            insta = InstaHandler()
            insta.post_text_story(roast_text, bg_color=(30, 30, 30))
            print("self disrespecvt posted to Instagram successfully.")
        except Exception as e:
            print(f"Instagram post failed: {e}")

        # Execute payout (demo mode)
        try:
            payout = RazorpayPayout()
            result = payout.send_money(
                name="Friend Name",
                ifsc="HDFC0001234",
                acc_no="1234567890",
                email="friend@email.com",
                phone="9123456789",
                amount_rupees=1,  # Demo amount
                purpose="punishment"
            )
            print("Payout result:", result)
        except Exception as e:
            print(f"Payout failed: {e}")

    else:
        print("No punishment required today.")


if __name__ == "__main__":
    main()
