from instagram_private_api import Client, ClientCompatPatch
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("INSTAGRAM_USERNAME")
password = os.getenv("INSTAGRAM_PASSWORD")
target_username = os.getenv("INSTAGRAM_TARGET_USERNAME")

api = Client(username, password)

user_info = api.username_info(target_username)

user_id = user_info['user']['pk']

user_feed = api.user_feed(user_id)

latest_post = user_feed['items'][0]

post_url = f"https://www.instagram.com/p/{latest_post['code']}/"

print('Latest post URL:', post_url)
