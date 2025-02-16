import unittest
from tests.login_tests import LoginTests

# Ładujemy testy z Test Case
login_tests = unittest.TestLoader().loadTestsFromTestCase(LoginTests)

# Lista testów do uruchomienia
tests_for_run = [
    login_tests,
    # ....
    # .....
]

# Łączymy testy w Test Suitę
test_suite = unittest.TestSuite(tests_for_run)

# Odpal testy
unittest.TextTestRunner().run(test_suite)