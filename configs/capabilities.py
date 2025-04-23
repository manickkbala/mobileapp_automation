"""
This module contains device capabilities for different iOS devices and environments.
"""

from appium.options.ios import XCUITestOptions

def get_iphone_16_pro_capabilities():
    """Returns capabilities for iPhone 16 Pro"""
    options = XCUITestOptions()
    options.platform_name = 'iOS'
    options.automation_name = 'XCUITest'
    options.device_name = 'iPhone 15'
    options.app = '/Users/balamurugan/Documents/automation_app/foodRx.app'
        # 🔧 Add the timeout here
    options.set_capability("wdaLaunchTimeout", 120000)
    options.no_reset = True
    options.set_capability("autoAcceptAlerts", True)
    return options

# Add more capability sets for different devices/environments as needed
# def get_iphone_15_pro_capabilities():
#     """Returns capabilities for iPhone 15 Pro"""
#     options = XCUITestOptions()
#     options.platform_name = 'iOS'
#     options.automation_name = 'XCUITest'
#     options.device_name = 'iPhone 15 Pro'
#     options.app = 'path/to/app'
#     options.no_reset = True
#     return options
