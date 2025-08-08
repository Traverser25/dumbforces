# DumbForces

**DumbForces** is a playful automation project that runs as a cron job to check if a user has solved a certain number of problems on [Codeforces](https://codeforces.com).  

If the user **fails** to meet the target, the script:  
1. Posts a *"disrespect"* message as an Instagram story.  
2. Sends money to a friend (because consequences hurt more when they're financial).

---

## Features
- **Codeforces Progress Check** – Tracks problem-solving activity.
- **Automated Instagram Story Posting** – Uses `instagrapi` to post stories directly.
- **Automatic Payment to Friend** – Sends money via Razorpay Payouts.
- **Cron Job Ready** – Designed to run periodically without manual intervention.
- **Logging** – Saves execution logs for review.

---

## Requirements
- Python 3.8+
- Codeforces handle
- Instagram credentials
- Razorpay API keys

---

## Installation
```bash
git clone https://github.com/Traverser25/dumbforces.git
cd dumbforces
pip install -r requirements.txt

CF_HANDLE=your_codeforces_handle
IG_USERNAME=your_instagram_username
IG_PASS=your_instagram_password
RAZORPAY_KEY=your_razorpay_key
RAZORPAY_SECRET=your_razorpay_secret
FRIEND_ACCOUNT=recipient_account_details

run manually to test
python main.py

## Disclaimer

This project was made **for fun**.  
Use it responsibly — especially the money-sending part.  
💸 Your wallet has feelings too.

