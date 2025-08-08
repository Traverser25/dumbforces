import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DisrespectHandler:
    def __init__(self, api_key_env="GROQ_API_KEY", model_env="GROQ_MODEL", endpoint="https://api.groq.com/openai/v1/chat/completions"):
        self.api_key = os.getenv(api_key_env)
        self.model = os.getenv(model_env, "llama-3.3-70b-versatile")
        self.endpoint = endpoint
        if not self.api_key:
            raise ValueError("Missing GROQ_API_KEY in environment (.env)")

    def generate_roasts(self, target="me", tone="campy, extra, flamboyant", count=8):
        prompt = f"Write {count} roast lines for '{target}' in a {tone} style. Keep it short, sharp, funny, and in Hindi."
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model,
            "temperature": 0.9,
            "max_tokens": 1025,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Tu ek Indian CarryMinati-style savage roaster hai jo apne aap ko roast kar raha hai. "
                        "Hindi me baat kar, sarcasm maar, apne aap ko insult kar confidently jaise 'main hi sabse bada bewakoof'. "
                        "Indian pop culture references use kar, filmy dialogues ghusa, aur short lines (50-100 words) banade."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        try:
            response = requests.post(self.endpoint, headers=headers, json=data, timeout=30)
            response.raise_for_status()
            content = response.json()["choices"][0]["message"]["content"]
            roasts = [line.strip(" \"'-") for line in content.splitlines() if line.strip()]
            return roasts[:count]
        except Exception:
            return None

# if __name__ == "__main__":
#     dh = DisrespectHandler()
#     r = dh.generate_roasts(target="lazy me and coding  consistency", tone="extra dramatic aur flamboyant", count=5)
#     if r:
#         for i, line in enumerate(r, 1):
#             print(f"{i}. {line}")
#     else:
#         print("AI ne roast se pehle hi resign de diya .")
