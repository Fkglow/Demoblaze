from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginpageLocators:
    LOG_IN_BUTTON = (By.XPATH, '//button[@onclick="logIn()"]')
    USERNAME_INPUT = (By.ID, 'loginusername')
    PASSWORD_INPUT = (By.ID, 'loginpassword')

class LoginPage(BasePage):
    """
    Login Page object
    """

    def enter_username(self, username):
        """
        Enters username
        :param username:
        """
        el = self.driver.find_element(*LoginpageLocators.USERNAME_INPUT)
        self.wait_5s.until(EC.element_to_be_clickable(el))
        el.send_keys(username)

    def enter_password(self, password):
        """
        Enters password
        :param password:
        """
        el = self.driver.find_element(*LoginpageLocators.PASSWORD_INPUT)
        self.wait_5s.until(EC.element_to_be_clickable(el))
        el.send_keys(password)

    def click_log_in(self):
        """
        Waits max 5 seconds for Log in button and clicks it
        :return:
        """
        el = self.driver.find_element(*LoginpageLocators.LOG_IN_BUTTON)
        self.wait_5s.until(EC.element_to_be_clickable(el))
        el.click()

    def get_alert_message(self):
        """
        Waits max 5  seconds for alert and returns its text
        :return: alert text
        """
        self.wait_5s.until(EC.alert_is_present())
        return self.alert.text

    def confirm_alert(self):
        """
        Confirms alert (Clicks OK)
        """
        self.alert.accept()

    def _verify_page(self):
        print("Weryfikacja strony logowania")
        self.wait_5s.until(EC.visibility_of_element_located(LoginpageLocators.USERNAME_INPUT))
        self.wait_5s.until(EC.visibility_of_element_located(LoginpageLocators.PASSWORD_INPUT))
        log_in_button = self.driver.find_element(*LoginpageLocators.LOG_IN_BUTTON)
        self.wait_5s.until(EC.element_to_be_clickable(log_in_button))
