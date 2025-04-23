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

def test_log_vitals():
    driver = webdriver.Remote(APPIUM_SERVER_URL, options=get_driver_options())
    wait = WebDriverWait(driver, DEFAULT_WAIT_TIME)

    try:
        
        # Step 1: click on Plus icon
        tap_by_coordinates(driver, 184, 800)

        # Step 2: click on vitals card
        vitals_card = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "//XCUIElementTypeOther[@name='Vitals']"
        )))
        vitals_card.click()

        # Step 3: click on Blood pressure
        blood_pressure_card = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Blood pressure'])[3]"
        )))
        blood_pressure_card.click()

        # Step 4: Enter sys
        sys_field = wait.until(EC.presence_of_element_located((
            AppiumBy.XPATH,
            "(//XCUIElementTypeOther[@name='Sys'])[2]/XCUIElementTypeOther[1]/XCUIElementTypeTextField"
        )))
        sys_field.clear()
        sys_field.send_keys("120")

        # Step 5: Enter sys
        dia_field = wait.until(EC.presence_of_element_located((
            AppiumBy.XPATH,
            "(//XCUIElementTypeOther[@name='Dia'])[2]/XCUIElementTypeOther[1]/XCUIElementTypeTextField"
        )))
        dia_field.clear()
        dia_field.send_keys("80")

        # Step 6: Save button
        save_button = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH,
            "(//XCUIElementTypeOther[@name='Save'])[2]"
        )))
        save_button.click()

        # Step 7: back button
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
