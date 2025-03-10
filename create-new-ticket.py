from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import os
import sys

from variables import main_URL, rm_filtered_URL, username, password, rm_path_to_screenshots, js_path_to_screenshots, js_filtered_URL, mb_filtered_URL, mb_path_to_screenshots


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

driver.get(rm_filtered_URL)

time.sleep(4)

# The next element is inside of an iframe which you have to swap to before you can find any elemnents within it

driver.switch_to.frame(0)

rm_file_path = (rm_path_to_screenshots)


# This will check to see if there is a splash that shows there are no tickets available and if it's there, it will terminate the script since theres no point in taking a screenshot of a blank queue
while True:
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'list-flavin')))
        print("No tickets found for Richard, moving to next technician.")
        break
    except Exception as e:
        print("Tickets found, script continuing.")
        driver.save_full_page_screenshot(rm_path_to_screenshots)
        print(f"Richard's tickets have been saved to {rm_file_path}")
        break

# Technician 2 block

driver.get(js_filtered_URL)

time.sleep(4)

driver.switch_to.frame(0)

js_file_path = (js_path_to_screenshots)


while True:
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'list-flavin')))
        print("No tickets found for Jerome, moving to next techncian.")
        break
    except Exception as e:
        print("Tickets found, script continuing.")
        driver.save_full_page_screenshot(js_file_path)
        print(f"Jerome's tickets have been saved to {js_file_path}")
        break    

# End technician 2 block

# Technician 3 block

mb_file_path = mb_path_to_screenshots

driver.get(mb_filtered_URL)

time.sleep(4)

driver.switch_to.frame(0)


while True:
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'list-flavin')))
        print("No tickets found for Miguel, scraping terminated.")
        driver.quit()
        break
    except Exception as e:
        print("Tickets found, script continuing.")
        driver.save_full_page_screenshot(mb_file_path)
        print(f"Miguel's tickets have been saved to {mb_file_path}")
        break    

# End technician 3 block


# Quick sleep to ensure the PA flow finds the screenshots and sends the email as intended
time.sleep(240)


#This deletes all the files after your script is finished so that it doesn't clog your storage and you don't have to worry about overwriting it next time you run it
try:
    os.remove(rm_file_path)
    print(f"File '{rm_file_path}' deleted successfully.")
except FileNotFoundError:
    print(f"Error: File '{rm_file_path}' not found.")
except PermissionError:
    print(f"Error: Permission denied to delete '{rm_file_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
try:
    os.remove(js_file_path)
    print(f"File '{js_file_path}' deleted successfully.")
except FileNotFoundError:
    print(f"Error: File '{js_file_path}' not found.")
except PermissionError:
    print(f"Error: Permission denied to delete '{js_file_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

try:
    os.remove(mb_file_path)
    print(f"File '{mb_file_path}' deleted successfully.")
except FileNotFoundError:
    print(f"Error: File '{mb_file_path}' not found.")
except PermissionError:
    print(f"Error: Permission denied to delete '{mb_file_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


driver.quit()
sys.exit()