from time import sleep

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



# code that HAS TO BE CHANGED -->



# =============================

# LinkedIn username and password in order to login
LINKED_IN_USERNAME = ""
LINKED_IN_PASSWORD = ""

# You need to have chromedriver latest version installed to run this program
linked_in_driver = webdriver.Chrome(service=Service("C:\Development\chromedriver.exe"))

# The job that you want to apply for
DESIRED_JOB = "Python Developer"

# =============================

linked_in_link = "https://www.linkedin.com/feed/"

linked_in_driver.get(linked_in_link)

# logining in linkedin
# =============================

button = linked_in_driver.find_element(By.CLASS_NAME, "main__sign-in-link")
# sleep(2)
button.click()

# sleep(2)

bar = linked_in_driver.find_element(By.ID, "username")
bar.send_keys(LINKED_IN_USERNAME)
# sleep(2)
bar = linked_in_driver.find_element(By.ID, "password")
bar.send_keys(LINKED_IN_PASSWORD)
# sleep(2)

button = linked_in_driver.find_element(By.CLASS_NAME, "login__form_action_container").find_element(By.TAG_NAME, "button")
button.click()

# this is to ensure that if LinkedIn requires some additional checking to log into your account,
# you could do it and then continue the program without breaking it
print("Please confirm that you are logged in")
input()

# =============================

# searching for "python developer" jobs
# =============================

bar = linked_in_driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
bar.send_keys(DESIRED_JOB+Keys.ENTER)

sleep(5)

button = linked_in_driver.find_element(By.CLASS_NAME, 'search-reusables__filter-list').find_elements(By.TAG_NAME, "li")
for li in button:
    if "Job" in li.find_element(By.TAG_NAME, "button").text:
        button = li.find_element(By.TAG_NAME, "button")
button.click()

print("Starting to apply for jobs...")

# =============================

# applying for jobs
# =============================
sleep(5)

jobs_list = linked_in_driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")

for i in range(len(jobs_list)):
    sleep(3)
    try:
        if "Easy Apply" in jobs_list[i].find_element(By.CLASS_NAME, "job-card-list__footer-wrapper").find_element(By.CLASS_NAME, "job-card-container__apply-method").text:
            button = jobs_list[i].find_element(By.CLASS_NAME, "job-card-list__footer-wrapper").find_element(By.CLASS_NAME, "job-card-container__apply-method")
            button.click()
            button = linked_in_driver.find_element(By.CLASS_NAME, "jobs-unified-top-card").find_element(By.CLASS_NAME, "jobs-save-button")
            button.click()
    except selenium.common.exceptions.NoSuchElementException:
        pass
# =============================
input()
