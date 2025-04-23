from appium.options.ios import XCUITestOptions
import os
from .capabilities import get_iphone_16_pro_capabilities

# Get the project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Server Configuration
APPIUM_SERVER_URL = 'http://localhost:4723/wd/hub'

# Test Credentials
TEST_EMAIL = 'va_jacy@mail.com'
TEST_PASSWORD = 'Passw0rd'

# Wait Times
DEFAULT_WAIT_TIME = 10
TRANSITION_WAIT_TIME = 5

def get_driver_options():
    """Returns configured XCUITestOptions for Appium driver"""
    return get_iphone_16_pro_capabilities() 