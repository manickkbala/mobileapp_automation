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


def test_log_gut():
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
        gut_discomfort_card = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Gut discomfort'])[2]"
        )))
        gut_discomfort_card.click()

        # Step 4: click on outro 1
        gut_discomfort_outro_1 = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Next'])[2]"
        )))
        gut_discomfort_outro_1.click()  

        # Step 5: click on outro 2
        gut_discomfort_outro_2 = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Next'])[2]"
        )))
        gut_discomfort_outro_2.click() 

         # Step 6: click on outro 3
        gut_discomfort_outro_3 = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Next'])[2]"
        )))
        gut_discomfort_outro_3.click()

        # Step 7: click on outro 4
        gut_discomfort_outro_4 = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Next'])[2]"
        )))
        gut_discomfort_outro_4.click()       

        # Step 8: click on outro 4
        gut_discomfort_outro_5 = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Next'])[2]"
        )))
        gut_discomfort_outro_5.click() 

        # Step 9: click on discomfort type
        discomfort_type = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Bloating'])[3]"
        )))
        discomfort_type.click() 

        # Dump page source to help debug
        # with open("after_tap_page_source.xml", "w", encoding="utf-8") as f:
        #     f.write(driver.page_source)

        # Step 10: click on severity 
        time.sleep(1)
        tap_by_coordinates(driver, 55, 552)
        
        # severity_5 = wait.until(EC.element_to_be_clickable((
        #     AppiumBy.XPATH,
        #     "//XCUIElementTypeOther[@name='0 1 2 3 4 5 6 7 8 9 10']/XCUIElementTypeOther[6]"
        # )))
        # severity_5.click()

        # Step 11: click on duration
        discomfort_type = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='1-2 hours'])[2]"
        )))
        discomfort_type.click() 

        # Step 12: click on secondary discomfort
        # Define swipe helper
        def swipe_up(driver):
            size = driver.get_window_size()
            start_x = size['width'] / 2
            start_y = size['height'] * 0.7
            end_y = size['height'] * 0.3

            driver.execute_script("mobile: swipe", {
                "direction": "up",
                "gestureOrigin": {"x": start_x, "y": start_y}
            })

        # Define scroll + click helper
        def scroll_until_visible_and_click(driver, wait, xpath, max_scrolls=10):
            for i in range(max_scrolls):
                try:
                    element = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath)))
                    element.click()
                    return
                except Exception:
                    print(f"🔁 Scroll attempt {i+1} — element not found. Swiping up.")
                    swipe_up(driver)
            raise Exception("❌ Could not find the element after scrolling.")

        # Use it here
        scroll_until_visible_and_click(
            driver,
            wait,
            "(//XCUIElementTypeOther[@name='Gassiness'])[2]"
        )

        # Step 13: Enter notes
        discomfort_notes = wait.until(EC.presence_of_element_located((
            AppiumBy.XPATH,
            "//XCUIElementTypeTextView[@name='Anything else we should know?']"
        )))
        discomfort_notes.clear()
        discomfort_notes.send_keys("My notes")
        # Try to close keyboard
        try:
             driver.hide_keyboard()
        except:
            print("⚠️ hide_keyboard didn't work, tapping outside...")
            driver.execute_script("mobile: tap", {"x": 200, "y": 400})
    
        # Step 11: Submit button
        submit_button = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH,
            "//XCUIElementTypeOther[@name='Submit']"
        )))
        submit_button.click()
        time.sleep(1)

        # Step 12: back button
        back_button = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH,
            "//XCUIElementTypeOther[@name='Back']"
        )))
        back_button.click()
        time.sleep(1)


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
