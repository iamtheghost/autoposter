from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os 
from dotenv import load_dotenv

import random

import time
from time import sleep

# Load environment variables from the .env file
load_dotenv()

def main():
    # Set up Facebook login account name and password
    account = os.getenv("FBACCOUNTEMAIL")
    password = os.getenv("FBPASS")

    # Set up Facebook groups to post, you must be a member of the group
    # This is an array, but can be a single index. Add multiple groups as
    # strings in the array to post to multiple
    groups_links_list = [
        "https://www.facebook.com/groups/814570613748960"
    ]

    # Set up text content to accompany posts
    # This can be canned text that will get added to each post randomly
    # The more general the better, i.e. "Check out this cool product on Amazon!"
    message = [
        "I found this video useful, maybe it will help you?", 
        "Checkout this new product.", 
        "Does anyone have any familiarity with this course?", 
        "Cool video on coding:"]

    # An array of YouTube links to post
    # this could be anything, whole objects referenced from another file,
    # canned text, URLs, anything

    youtube_links = [
        "https://youtu.be/",
        "https://youtu.be/",
        "https://youtu.be/",
        "https://youtu.be/",
        "https://youtu.be/"
    ]


    # Set up paths of images to post
    # Using this array, you could also add a series of images to accompany posts made
    # in the groups defined above
    images_list = []

    # Setup login process flow to Facebook
    options = webdriver.ChromeOptions()

    # You will need to update this to point to YOUR browser binary location
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google\ Chrome"

    # Change YOURUSERNAME to your local username if on Mac. You'll need to change this accordingly if you're 
    # using Windows or Linux
    options.add_argument("user-data-dir=/Users/YOURUSERNAME/Library/Application Support/Google/Chrome/Default")
    
    # Optional preferences
    #prefs = {"profile.default_content_setting_values.notifications" : 2}
    #options.add_experimental_option("prefs",prefs)
    
    # Attempt to login
    # TO DO: Add intelligent failure/retry attempts
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.facebook.com')
    try:
        emailelement = driver.find_element(By.XPATH,'//*[@id="email"]').send_keys(account)
    except:
        pass
    
    try:
        passelement = driver.find_element(By.XPATH,'//*[@id="pass"]').send_keys(password)
    except:
        pass
    
    
    #Pauses the code to let the page load, adjust for slower internet connections
    time.sleep(1)
    #Accepts all cookies
    try:
        cookieselement = driver.find_element(By.XPATH, '//*[@data-cookiebanner="accept_button"]').click()
        time.sleep(2)
    except:
        pass
    
    try:
        loginelement = driver.find_element(By.XPATH,'//*[@name="login"]').click()
    except:
        pass

    time.sleep(4)

    # Post on each group from the array above
    for group in groups_links_list:
        driver.get(group)
        time.sleep(2)
        if message != "":
            #Finds and selects the text field in the post
            post_box = driver.find_element(By.XPATH,"//*[text()='Write something...']")
            time.sleep(3)
            post_box.click()
            time.sleep(3)
            post_text_parent = driver.find_element(By.XPATH,"//div[@aria-label='Write something...']")
            time.sleep(3)
            post_text_parent.send_keys(message)
            time.sleep(3)
            youtube_link = random.choice(youtube_links)
            post_text_parent.send_keys(youtube_link)
            time.sleep(4)
            #Finds the button to send the post
            post_button = driver.find_element(By.XPATH,"//div[@aria-label='Post']")
            time.sleep(3)
            post_button.click()
        time.sleep(10)
        
    # Close driver
    #driver.close()

if __name__ == '__main__':
  main()
