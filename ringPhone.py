from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

email = "your apple ID email"
password = "your password"

def ring_phone():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options = options, executable_path="")
    driver.get("https://www.icloud.com/find") #go to find my device page
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"auth-frame")))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "account_name_text_field"))).send_keys(email)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "account_name_text_field"))).send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password_text_field"))).send_keys(password, Keys.ENTER)
    driver.switch_to.default_content()
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"find")))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "sc1517"))).click()
    driver.find_element_by_css_selector("[title^='your device name']").click()
    driver.find_element_by_css_selector("[title^='Play a sound on this iPhone']").click()
