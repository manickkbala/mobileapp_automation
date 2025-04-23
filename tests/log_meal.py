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

        # Step 2: click on meal card
        meal_card = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "//XCUIElementTypeOther[@name='Meal']"
        )))
        meal_card.click()

        # Step 3: click on mealUpload type
        mealupload_type = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "//XCUIElementTypeOther[@name='Select meal photo']"
        )))
        mealupload_type.click()

        # Step 4: select meal pics
        select_meal_pic = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "//XCUIElementTypeImage[@name='Photo, 31 March 2018, 12:44 AM']"
        )))
        select_meal_pic.click()
        time.sleep(1)

        driver.execute_script("mobile: tap", {"x": 200, "y": 400})

        # Step 5: Enter meal descriptions
        meal_desc = wait.until(EC.presence_of_element_located((
            AppiumBy.XPATH,
            "//XCUIElementTypeOther[@name='Description Optionally, add any details such as ingredients or brands to enhance our analysis.']"
        )))
        meal_desc.click()
        meal_desc.send_keys("french fries from automation")
        # Try to close keyboard
        try:
             driver.hide_keyboard()
        except:
            print("⚠️ hide_keyboard didn't work, tapping outside...")
            driver.execute_script("mobile: tap", {"x": 200, "y": 400})

        # Step 6: Submit button
        submit_button = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH,
            "(//XCUIElementTypeOther[@name='Submit'])[2]"
        )))
        submit_button.click()

        # Step 7: meal outro 1
        meal_outro_1 = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Next'])[2]"
        )))
        meal_outro_1.click()  

        # Step 8: meal outro 2
        meal_outro_2 = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Next'])[2]"
        )))
        meal_outro_2.click()   

        # Step 9: meal outro 3
        meal_outro_3 = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Next'])[2]"
        )))
        meal_outro_3.click()   

        # Step 10:  meal outro 4
        meal_outro_4 = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Done'])[2]"
        )))
        meal_outro_4.click()  

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
