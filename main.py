import time, os
from dotenv import load_dotenv
import logging

load_dotenv()
url = os.getenv('url')
api_key = os.getenv('api_key')
counter = 0
while counter<=5:
	print("I am working!")
	print(url)
	logging.info(f"api-key = {api_key}")
	
	time.sleep(3)
