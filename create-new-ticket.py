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
# Go to webpage
driver.get(url)

#Wait for element to be on screen
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


#Brief pause to wait for loading
time.sleep(2)


#This loop should try and click a couple of different sign in buttons, but was sometimes failing so I put in a loop to retry it until it's successful
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

# The next element is inside of an iframe which you have to swap to before you can find any elemnents within it

driver.switch_to.frame(0)


# This will check to see if there is a splash that shows there are no tickets available and if it's there, it will terminate the script since theres no point in taking a screenshot of a blank queue
while True:
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'list-flavin')))
        print("No tickets found, script terminating.")
        driver.quit()
        sys.exit()
    except Exception as e:
        print("Tickets found, script continuing.")
        break
    

driver.save_full_page_screenshot(path_to_screenshots)


file_path = (path_to_screenshots)

time.sleep(240)


#This deletes the file after your script is finished so that it doesn't clog your storage and you don't have to worry about overwriting it next time you run it
try:
    os.remove(file_path)
    print(f"File '{file_path}' deleted successfully.")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except PermissionError:
    print(f"Error: Permission denied to delete '{file_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
