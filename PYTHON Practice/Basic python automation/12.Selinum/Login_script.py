from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
username = driver.find_element(By.ID,"username")
password = driver.find_element(By.ID,"password")
username.send_keys("rahulsharma")
password.send_keys("SuperSecreatePass")
login_button = driver.find_element(By.CSS_SELECTOR,"button.radius")
login_button.click()
input("Press Enter to close...")
driver.quit()
