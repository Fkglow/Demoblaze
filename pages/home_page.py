from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class HomePageLocators:
    """
    Home Page locators
    """
    LOG_IN_A = (By.ID, "login2")        # mam w 1 miejscu tez lokator, wiec jak zmieni sie nie tylko id a tez id>xpath to fik i gotowe
    # CONTACT_A = (By.ID, )
    NAME_OF_USER_A = (By.ID, "nameofuser")
    LOG_OUT_A = (By.ID, "logout2")
    SIGN_UP_A = (By.ID, "signin2")

class HomePage(BasePage):
    """
    Home Page object
    """

    def check_if_log_out_is_clickable(self):
        return self.wait_5s.until(EC.element_to_be_clickable(HomePageLocators.LOG_OUT_A))

    def get_welcome_username_text(self):
        """
        Gets Welcome <USERNAME> message from the top right of the page
        :return: Welcome <USERNAME> text
        """
        el = self.wait_5s.until(EC.visibility_of_element_located(HomePageLocators.NAME_OF_USER_A))
        return el.text

    def click_log_in(self):
        """
        Clicks log in link
        :return:LoginPage instance
        """
        # 1. Znajdź przycisk log in
        # 2. Kliknij w niego
        self.driver.find_element(*HomePageLocators.LOG_IN_A).click()        # "*" rozpakowuje, np jeśli mam krotkę (1,2) --> to *(1,2) zmienia się w 1,2
        # Zwróć stronę logowania
        return LoginPage(self.driver)

    def click_log_out(self):
        """
        Clicks Log out link
        """
        self.driver.find_element(*HomePageLocators.LOG_OUT_A).click()

    def get_login_text(self):
        self.wait_5s.until(EC.text_to_be_present_in_element(HomePageLocators.LOG_IN_A, "Log in"))
        return self.driver.find_element(*HomePageLocators.LOG_IN_A).text

    def get_sign_up_text(self):
        self.wait_5s.until(EC.text_to_be_present_in_element(HomePageLocators.SIGN_UP_A, "Sign up"))
        return self.driver.find_element(*HomePageLocators.SIGN_UP_A).text

    def click_contact(self):
        """
        Clicks log in link
        :return:
        """
        # TODO:

    def _verify_page(self):
        #TODO:
        print("Weryfikacja strony głównej")
        assert self.driver.title == "STORE"

