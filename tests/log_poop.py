import time
import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from log_weight import tap_by_coordinates


# Import config values
from configs.config import (
    get_driver_options,
    APPIUM_SERVER_URL,
    DEFAULT_WAIT_TIME,
    TRANSITION_WAIT_TIME
)


def test_log_poop():
    driver = webdriver.Remote(APPIUM_SERVER_URL, options=get_driver_options())
    wait = WebDriverWait(driver, DEFAULT_WAIT_TIME)

    try:
        
        # Step 1: click on Plus icon
        tap_by_coordinates(driver, 184, 800)

        # Step 2: click on cut card
        gut_card = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "//XCUIElementTypeOther[@name='Gut']"
        )))
        gut_card.click()

        # Step 3: click on Gut discomfort sub card
        poop_card = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Poop'])[2]"
        )))
        poop_card.click()

        # Step 2: click on iutro 1
        poop_intro_1 = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Next'])[2]"
        )))
        poop_intro_1.click()  

        # Step 3: click on outro 2
        poop_intro_2 = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Next'])[2]"
        )))
        poop_intro_2.click()  

        # Step 4: click on outro 3
        poop_intro_3 = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Next'])[2]"
        )))
        poop_intro_3.click()  

        # Step 5: click on outro 4
        poop_intro_4 = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Next'])[2]"
        )))
        poop_intro_4.click()  

        # Step 6: click on outro 5
        poop_intro_5 = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Next'])[2]"
        )))
        poop_intro_5.click()  

        # Step 7: click on Bristol type 
        bristol_type = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Type 3 | Sausage-like'])[3]"
        )))
        bristol_type.click()  

        # Step 8: Enter notes
        poop_notes = wait.until(EC.presence_of_element_located((
            AppiumBy.XPATH,
            "//XCUIElementTypeTextView[@name='Anything else we should know?']"
        )))
        poop_notes.clear()
        poop_notes.send_keys("My poop notes")
        # Try to close keyboard
        try:
             driver.hide_keyboard()
        except:
            print("⚠️ hide_keyboard didn't work, tapping outside...")
            driver.execute_script("mobile: tap", {"x": 200, "y": 400})
  
        # Step 9: Enter times of poop
        discomfort_notes = wait.until(EC.presence_of_element_located((
            AppiumBy.XPATH,
            "//XCUIElementTypeTextField[@value='  Type here']"
        )))
        discomfort_notes.clear()
        discomfort_notes.send_keys('2')
        # Try to close keyboard
        try:
             driver.hide_keyboard()
        except:
            print("⚠️ hide_keyboard didn't work, tapping outside...")
            driver.execute_script("mobile: tap", {"x": 200, "y": 400})
  
        # Step 10: Submit button
        submit_button = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH,
            "//XCUIElementTypeOther[@name='Submit']"
        )))
        submit_button.click()

        # Step 11: back button
        back_button = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH,
            "//XCUIElementTypeOther[@name='Back']"
        )))
        back_button.click()

    except Exception as e:
        screenshot_name = "screenshot_profile_failure.png"
        driver.save_screenshot(screenshot_name)
        print(f"\n❌ Profile test failed")
        print(f"📸 Screenshot saved: {screenshot_name}")
        print(f"🛠 Error: {str(e)}")
        try:
            print("🔍 Page snippet:\n", driver.page_source[:800])
        except:
            print("⚠️ Could not fetch page source.")
        raise e

    finally:
        driver.quit()
