from instagrapi import Client
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont
import os
import tempfile
import textwrap

load_dotenv()

class InstaHandler:
    def __init__(self):
        self.client = Client()
        self.username = os.getenv("IG_USERNAME")
        self.password = os.getenv("IG_PASS")

    def login(self):
        try:
            self.client.login(self.username, self.password)
        except Exception as e:
            raise RuntimeError(f"Instagram login failed: {e}")

    def post_story(self, image_path, caption=""):
        self.login()
        try:
            self.client.photo_upload_to_story(image_path, caption)
            print("✅ Story posted successfully")
        except Exception as e:
            raise RuntimeError(f"Failed to post story: {e}")

    def post_text_story(self, text, bg_color=(0, 0, 0), text_color=(255, 255, 255)):
        self.login()

        img = Image.new("RGB", (1080, 1920), color=bg_color)
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("arial.ttf", 60)
        except:
            font = ImageFont.load_default()

        wrapped_text = textwrap.fill(text, width=20)

        bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=font, align="center")
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        position = ((1080 - w) / 2, (1920 - h) / 2)

        draw.multiline_text(position, wrapped_text, font=font, fill=text_color, align="center")

        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
            img.save(tmp.name)
            temp_path = tmp.name

        try:
            self.client.photo_upload_to_story(temp_path, "")
            print("Text story posted successfully")
        except Exception as e:
            raise RuntimeError(f"Failed to post text story: {e}")
        finally:
            os.remove(temp_path)


# if __name__ == "__main__":
#     insta = InstaHandler()
#     insta.post_text_story("Hello Instagram! This is a text story", bg_color=(30, 30, 30))
