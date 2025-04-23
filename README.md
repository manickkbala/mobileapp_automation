# Ask Digbi Chatbot Test Automation Framework

This framework automates testing of the Ask Digbi chatbot in the iOS mobile app using Appium and Python.

## Prerequisites

1. Python 3.9+
2. Xcode with iOS Simulator
3. Appium Server
4. iOS App (.app file)

## Setup

1. Install dependencies:
```bash
pip3 install -r requirements.txt
```

2. Configure the iOS simulator settings in `configs/test_config.py`:
- Update `platformVersion` to match your simulator
- Update `deviceName` to match your simulator
- Ensure the app path is correct

3. Place your iOS app (.app file) in the `app` directory

## Running Tests

1. Start Appium server:  pkill -f appium
```bash
appium --base-path /wd/hub

2. Run the tests:
```bash
python3 -m pytest test_login.py -v
```



## Framework Structure

- `configs/`: Configuration files
- `tests/`: Test implementation
- `utils/`: Utility functions for response scoring
- `reports/`: Generated test reports
- `app/`: iOS app file

## CI Integration

The framework is ready for CI integration. Key features:
- Modular test structure
- Configurable test parameters
- Detailed reporting
- Error handling and logging

## To run tests in a specific order using pytest, use the pytest-order plugin:
pip install pytest-order
