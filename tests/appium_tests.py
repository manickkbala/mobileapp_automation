
# appium_test.py

from test_login import test_login_flow
from log_weight import test_log_weight
from log_vitals import test_log_vitals
from log_gut import test_log_gut
from log_poop import test_log_poop

def run_all_tests():
    print("\n🚀 Running login test...")
    test_login_flow()
    
    print("\n✅ Login weight completed. Running log weight test...")
    test_log_weight()

    print("\n✅ Login blood pressure completed. Running log vitals test...")
    test_log_vitals()

    print("\n✅ Login discomfort completed. Running log gut test...")
    test_log_gut()

    print("\n✅ Login poop completed. Running log poop test...")
    test_log_poop()

    print("\n🎉 All tests completed.")

if __name__ == "__main__":
    run_all_tests()


# pytest.main([
#     "tests/test_login.py",
#     "tests/log_weight.py",
# ])