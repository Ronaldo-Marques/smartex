from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

url = 'https://demoqa.com/automation-practice-form'
browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()

#indentificacao
firstName = browser.find_element("id","firstName")
firstName.send_keys("Ronaldo")
lastName = browser.find_element("id","lastName")
lastName.send_keys("Marques")
email = browser.find_element("id","userEmail")
email.send_keys("ronaldobcmarques@hotmail.com")

#genero
gender = browser.find_element(By.XPATH,'//*[@id="gender-radio-1"]')

#mobile
mobile = browser.find_element("id", "userNumber")
mobile.send_keys("915649895")

#data nascimento
date = browser.find_element("id", "dateOfBirthInput")
date.send_keys("01 Jul 1997")

#subjects
subjects = browser.find_element("id", "subjectsInput")
subjects.send_keys("Maths, Science, Physics")

#hobbies
hobbies1 = browser.find_element(By.XPATH,'//*[@id="hobbies-checkbox-1"]')
hobbies2 = browser.find_element(By.XPATH,'//*[@id="hobbies-checkbox-3"]')

#address
address = browser.find_element("id", "currentAddress")
address.send_keys("Gondomar, Porto, Portugal")

browser.quit()