import time
import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import config values
from configs.config import (
    get_driver_options,
    APPIUM_SERVER_URL,
    TEST_EMAIL,
    TEST_PASSWORD,
    DEFAULT_WAIT_TIME,
    TRANSITION_WAIT_TIME
)

def test_login_flow():
    driver = webdriver.Remote(APPIUM_SERVER_URL, options=get_driver_options())
    wait = WebDriverWait(driver, DEFAULT_WAIT_TIME)

    try:

        # Step 1: Tap "Sign in with email or phone"
        sign_in_button = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH,
            "//XCUIElementTypeOther[@name='Sign in with email or phone']"
        )))
        sign_in_button.click()

        # Step 2: Enter Email
        email_field = wait.until(EC.presence_of_element_located((
            AppiumBy.XPATH,
            "//XCUIElementTypeTextField[@placeholderValue='Phone or email']"
        )))
        email_field.clear()
        email_field.send_keys(TEST_EMAIL)
        time.sleep(1)

        # Step 3: Click Next
        next_button = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH,
            "//XCUIElementTypeOther[@name='Next'][@enabled='true']"
        )))
        next_button.click()

        # Step 4: Enter Password
        password_field = wait.until(EC.presence_of_element_located((
            AppiumBy.XPATH,
            "//XCUIElementTypeSecureTextField[@placeholderValue='Password']"
        )))
        password_field.send_keys(TEST_PASSWORD)
        time.sleep(1)

        # Step 5: Tap Sign In
        sign_in_final_button = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH,
            "//XCUIElementTypeOther[@name='Sign in'][@enabled='true']"
        )))
        sign_in_final_button.click()
        time.sleep(2)

        # Step 6: Verify Home screen is shown
        home_screen = wait.until(EC.presence_of_element_located((
            AppiumBy.XPATH,
            "(//XCUIElementTypeOther[@name='Dashboard'])[3]"
        )))
        assert home_screen.is_displayed(), "Login succeeded but Home screen not shown"
        # time.sleep(5)
           
        # Step 7: walthrough1
        walthrough_1 = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Next'])[3]"
        )))
        walthrough_1.click()

        # Step 8: walthrough2
        walthrough_2 = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Next'])[3]"
        )))
        walthrough_2.click()

        # Step 9: walthrough3
        walthrough_3 = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Next'])[3]"
        )))
        walthrough_3.click()

        # Step 10: walthrough4
        walthrough_4 = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Next'])[3]"
        )))
        walthrough_4.click()

        # # Step 11: walthrough5
        # walthrough_5 = wait.until(EC.element_to_be_clickable((
        #     AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Next'])[3]"
        # )))
        # walthrough_5.click()

        # Step 12: walthrough Done
        walthrough_done = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Done'])[3]"
        )))
        walthrough_done.click()
        
    except Exception as e:
        screenshot_name = "screenshot_login_failure.png"
        driver.save_screenshot(screenshot_name)
        print(f"\n❌ Login test failed")
        print(f"📸 Screenshot saved: {screenshot_name}")
        print(f"🛠 Error: {str(e)}")
        try:
            print("🔍 Page snippet:\n", driver.page_source[:800])
        except:
            print("⚠️ Could not fetch page source.")
        raise e

    finally:
        driver.quit()
