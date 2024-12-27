from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import random
from .proxy_manager import get_random_proxy
import time
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")



def fetch_trends():
    # Get a random proxy from the list
    proxy = get_random_proxy()

    # Setup headless Chrome options
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (without GUI)
    options.add_argument(f"--proxy-server={proxy}")  # Use the random proxy

    # Set path to the chromedriver executable
    service = Service('/path/to/chromedriver')  # Update with your chromedriver path
    driver = webdriver.Chrome(service=service, options=options)

    # Navigate to Twitter login page
    driver.get("https://twitter.com/login")
    driver.implicitly_wait(10)

    # Locate the username and password input fields and log in
    username_field = driver.find_element(By.NAME, "session[username_or_email]")
    password_field = driver.find_element(By.NAME, "session[password]")

    # Input the credentials and submit the login form
    username_field.send_keys(TWITTER_USERNAME)
    password_field.send_keys(TWITTER_PASSWORD)
    password_field.send_keys(Keys.RETURN)

    # Wait for the login to complete (you can adjust the wait time)
    time.sleep(5)  # Increase if necessary for slower networks or page load

    # Now, navigate to the trends page
    driver.get("https://twitter.com/explore/tabs/trending")
    driver.implicitly_wait(10)

    # Fetch the trending topics from the page
    trends = driver.find_elements(By.XPATH, "//div[@aria-label='Trending']")
    top_trends = [trend.text for trend in trends[:5]]  # Get the top 5 trends

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Organize the trend data
    trend_data = {
        "timestamp": timestamp,
        "trend1": top_trends[0],
        "trend2": top_trends[1],
        "trend3": top_trends[2],
        "trend4": top_trends[3],
        "trend5": top_trends[4],
        "ip_address": proxy
    }

    # Close the browser
    driver.quit()

    # Return the trend data to be stored in the database
    return trend_data
