
import os
import requests
import logging
from datetime import datetime
from dotenv import load_dotenv

# Load .env for CF_USERNAME
load_dotenv()

# Setup logger
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, "main.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class CodeforcesChecker:
    def __init__(self):
        self.handle = os.getenv("CF_USERNAME")
        self.api_url = f"https://codeforces.com/api/user.status?handle={self.handle}&from=1&count=10"

    def get_submissions(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            if data["status"] == "OK":
                logging.info(f"Successfully fetched submissions for user: {self.handle}")
                return data["result"]
            else:
                logging.error("Codeforces API returned non-OK status.")
                return []
        except requests.RequestException as e:
            logging.error(f"Request error while fetching Codeforces submissions: {e}")
            return []

    def get_accepted_today(self):
        today = datetime.now().date()
        submissions = self.get_submissions()
        count = 0
        seen_problems = set()  # Avoid counting same problem multiple times

        for sub in submissions:
            sub_time = datetime.fromtimestamp(sub["creationTimeSeconds"]).date()

            # print(sub_time ,";== ", today)
            if sub_time == today and sub.get("verdict") == "OK":
                problem_id = f"{sub['problem']['contestId']}-{sub['problem']['index']}"
                if problem_id not in seen_problems:
                    seen_problems.add(problem_id)
                    count += 1

        logging.info(f"User {self.handle} has {count} accepted submissions today.")
        return count
