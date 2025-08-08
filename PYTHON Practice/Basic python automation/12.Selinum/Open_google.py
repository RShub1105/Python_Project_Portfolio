# Here we can open the google search directly.
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.google.com")
input("Press Enter to close browser...")
driver.quit() 

# Search something automatacally.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME,'q')
search_box.send_keys("Github login")
search_box.send_keys(Keys.RETURN)
input("Presss Enter to close")
driver.quit()

