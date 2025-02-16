import test_data.test_data
from tests.base_test import BaseTest
from ddt import data, unpack, ddt
from test_data.test_data import DataReader

@ddt
class LoginTests(BaseTest):

    def setUp(self):
        super().setUp()     # wywołaj metodę z klasy nadrzędnej = BaseTest
        # dodatkowy warunek w setUpie
        self.login_page = self.home_page.click_log_in()

    def testEmptyLogin(self):
        # 1. Nie wpisujemy nic i klikamy login
        self.login_page.click_log_in()
        # 2. Sprawdź, czy wyświetla się alert "Please fill out Username and Password"
        self.assertEqual("Please fill out Username and Password.", self.login_page.get_alert_message())
        self.login_page.confirm_alert()

    @data(*DataReader.get_csv_data("../test_data/valid_login_credentials.csv"))
    @unpack
    def testValidLogin(self, username, password):
        #1. Wpisz login
        self.login_page.enter_username(username)
        #2. Wpisz haslo
        self.login_page.enter_password(password)
        #3. Kliknij login
        self.login_page.click_log_in()
        #4. Sprawdz, czy w prawym górnym rogu widnieje powitanie "Welcome tester_alk"
        welcome_text_act = self.home_page.get_welcome_username_text()
        self.assertEqual(f"Welcome {username}", welcome_text_act)
        #5. Sprawdz, czy mozna kliknąć Logout
        self.home_page.click_log_out()
        # Sprawdź czy przyciski zmieniły się na Log in i Sign up
        self.assertEqual(self.home_page.get_login_text(), "Log in")
        self.assertEqual(self.home_page.get_sign_up_text(), "Sign up")



