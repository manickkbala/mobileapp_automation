import time
import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# Import config values
from configs.config import (
    get_driver_options,
    APPIUM_SERVER_URL,
    DEFAULT_WAIT_TIME,
    TRANSITION_WAIT_TIME
)

def tap_by_coordinates(driver, x, y):
    try:
        print(f"👉 Tapping at coordinates ({x}, {y}) using mobile: tap...")
        driver.execute_script("mobile: tap", {"x": x, "y": y})
        print("✅ Tap performed successfully.")
    except Exception as e:
        print("❌ Failed to perform tap.")
        print("🛠 Error:", e)
        raise e


def test_log_weight():
    driver = webdriver.Remote(APPIUM_SERVER_URL, options=get_driver_options())
    wait = WebDriverWait(driver, DEFAULT_WAIT_TIME)

    try:
        # Step 1: click on Plus icon
        tap_by_coordinates(driver, 184, 800)

        # Step 2: click on weight card
        weight_card = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "//XCUIElementTypeOther[@name='Weight']"
        )))
        weight_card.click()

        # Step 3: Enter weight
        weight_field = wait.until(EC.presence_of_element_located((
            AppiumBy.XPATH,
            "//XCUIElementTypeTextField[@value='Type']"
        )))
        weight_field.clear()
        weight_field.send_keys("200")
        time.sleep(1)

        # Step 4: Submit button
        submit_button = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH,
            "(//XCUIElementTypeOther[@name='Submit'])[2]"
        )))
        submit_button.click()
        time.sleep(2)

        # Step 4: back button
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
