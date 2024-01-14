import time, os
from dotenv import load_env
import logging

load_env()
url = os.getenv('url')
api_key = os.getenv('api_key')
counter = 0
while counter<=5:
	print("I am working!")
	print(url)
	loggig.info(f"api-key = {api_key}")
	
	time.sleep(3)
