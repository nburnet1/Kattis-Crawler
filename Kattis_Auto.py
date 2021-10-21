##Noah Burnette
##Version 0.1
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import sys
import os

if len(sys.argv) != 5:
    print("Usage: <username/email> <password> <problem_ID> <file_location>")
    exit(0)

username = sys.argv[1]
password = sys.argv[2]
problem_ID = sys.argv[3]
file_location = sys.argv[4]


print("Initializing driver...")
driver = webdriver.Firefox()

def login(username,password):
    print("Logging in...")
    driver.get("https://open.kattis.com/login/email?")
    assert "Kattis" in driver.title
    elem = driver.find_element(By.ID,"user_input")
    elem.clear()
    elem.send_keys(username)
    elem = driver.find_element(By.ID,"password_input")
    elem.clear()
    elem.send_keys(password)
    elem = driver.find_element(By.CLASS_NAME, "btn-default")
    elem.click()

def get_problem(problem_ID):
    driver.get("https://open.kattis.com/problems/" + problem_ID)
    elem = driver.find_element(By.CLASS_NAME,"headline-wrapper")
    assert elem.text in driver.page_source
    print("Accessing '" + elem.text + "'")
    elem = driver.find_element(By.CLASS_NAME,"small")
    elem.click();
    
def upload_file(file_location):
    print("Uploading file...")
    elem = driver.find_element(By.ID,"sub_files_input")
    elem.send_keys(file_location)
    sleep(.5)
    elem = driver.find_element(By.CSS_SELECTOR, ".btn-default[type='submit']").click()
    print("Testing...")
    sleep(13)
    elem = driver.find_element(By.CSS_SELECTOR, ".middle[data-type='status']")
    print(elem.text)
    
login(username,password)
get_problem(problem_ID)
upload_file(file_location)













