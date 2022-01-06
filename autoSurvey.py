from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from dotenv import load_dotenv
load_dotenv()
import time


driver = webdriver.Chrome()
link = "https://secure.ctsext.it.ucla.edu/UCLACovidClearance/"
link2 = "https://uclasurveys.co1.qualtrics.com/jfe/form/SV_3qRLtouCYKzBbH7"
driver.get(link2)


studentSurveyButton = driver.find_element_by_id('QID3-2-label')
studentSurveyButton.click()
nextButton = driver.find_element_by_id('NextButton')
nextButton.click()


def login():
    username = os.environ['USERNAME']
    password = os.environ['PASSWORD']
    nameInput = driver.find_element_by_id('logon')
    nameInput.send_keys(username)
    passInput = driver.find_element_by_id('pass')
    passInput.send_keys(password)
    submitButton = driver.find_element_by_xpath('//*[@id="sso"]/form/div/table/tbody/tr/td[1]/button')
    submitButton.click()

def next():
    nextButton = driver.find_element_by_id('NextButton')
    nextButton.click()

def doQuestion(ans, pause):
    time.sleep(pause)
    choice = driver.find_element_by_id(ans)
    choice.click()
    next()

time.sleep(2)
login()

time.sleep(2)
driver.switch_to.frame("duo_iframe")
idBtn = driver.find_elements_by_xpath('//*[@id="auth_methods"]/fieldset[2]/div/button')
idBtn[0].click()
# touchIDbttn = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/form/div[1]/fieldset[2]/div/button')
# touchIDbttn.click()
# btn = WebDriverWait(driver, 30).until(
#         EC.presence_of_element_located((By.ID, "NextButton"))
#     )
# btn.click()

# time.sleep(1)
# next()

# answers = ['QID215-2-label', 'QID207-4-label', 'QID2-1-label', 'QID12-2-label', 'QID3-2-label', 'QID3-2-label']

# for answer in answers:
#     doQuestion(answer, 1)
