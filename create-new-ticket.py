from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import os
import sys

from variables import main_URL, Filtered_URL, username, password, path_to_screenshots


driver = webdriver.Firefox()

url = (main_URL)
driver.get(url)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "i0116"))
)

element = driver.find_element(By.ID, "i0116")
element.clear()
element.send_keys(username + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "i0118"))
)

element = driver.find_element(By.ID, "i0118")
element.clear()
element.send_keys(password)

time.sleep(2)

while True:
    try:
        check_input = driver.find_element(By.ID, "idSIButton9")
        check_input.click()

        time.sleep(1)

        check_input = driver.find_element(By.ID, "idSIButton9")
        check_input.click()
        break
    except Exception as e:
        print("Clicking button failed!", e)
        print("Retrying now...")

time.sleep(2)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Switch to full client")
link.click()

time.sleep(4)

driver.get(Filtered_URL)

time.sleep(4)

driver.switch_to.frame(0)

try:
    driver.find_element(By.CLASS_NAME, 'list-flavin')
    print("No tickets found, script terminating.")
    sys.exit()
except:
    print("Tickets found, script continuing.")
    

driver.save_full_page_screenshot(path_to_screenshots)


file_path = (path_to_screenshots)

time.sleep(240)

try:
    os.remove(file_path)
    print(f"File '{file_path}' deleted successfully.")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except PermissionError:
    print(f"Error: Permission denied to delete '{file_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")