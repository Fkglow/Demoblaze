from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert

class BasePage:
    """
    Base class for each page
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait_5s = WebDriverWait(self.driver, timeout=5)
        self.alert = Alert(self.driver)
        self._verify_page()     # każda strona będzie się automatycznie testowała jeśli będzie miała to verify_page

    def _verify_page(self):     # metoda prywatna, 2 podłogi to MEGA PRYWATNA (enkapsulacja)
        return

