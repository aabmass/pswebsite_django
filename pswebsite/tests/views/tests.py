from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from pswebsite.tests.test_types import SeleniumTest, ViewTest
from pswebsite.tests.test_settings import test_user_data

from pswebsite.forms import RegisterForm

class IndexViewTests(ViewTest):
    view_name = 'pswebsite:index'

    def test_shows_login_menu(self):
        res = self.get_res()
        self.assertContains(res, "Login")

    def test_shows_register_menu(self):
        res = self.get_res()
        self.assertContains(res, "Register")

class RegisterViewTests(SeleniumTest):
    def test_register_form_can_register_new_user(self):
        self.load_selenium_page('pswebsite:register')
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys("register@tester.com")
        first_name_input = self.selenium.find_element_by_name("first_name")
        first_name_input.send_keys("Regist")
        last_name_input = self.selenium.find_element_by_name("last_name")
        last_name_input.send_keys("Err")
        password1_input = self.selenium.find_element_by_name("password1")
        password1_input.send_keys("register")
        password2_input = self.selenium.find_element_by_name("password2")
        password2_input.send_keys("register")

        self.selenium.find_element_by_xpath('//input[@value="Create User"]').click()

        # now make sure the user is in the database
        user = User.objects.get(username="register@tester.com")
        self.assertIsNotNone(user)

    def test_register_form_logs_in_user_after_successful_registration(self):
        self.load_selenium_page('pswebsite:register')

class LoginLogoutViewTests(SeleniumTest):
    def __init__(self, *args, **kwargs):
        self.is_logged_in = False
        super().__init__(*args, **kwargs)

    # def setUp(self):
    #     super().setUp()
    #     (self.user, self.user_data) = create_new_user()

    def login_test_user(self):
        self.load_selenium_page('pswebsite:login')

        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(test_user_data['username'])
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys(test_user_data['password'])
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()

    def test_can_login_user(self):
        # try to log in the new user created above
        self.login_test_user()

        # to test, the user's name should appear at the index page
        #self.load_selenium_page(view_name='pswebsite:index')
        self.assertIn(test_user_data['username'],
                      self.selenium.find_element_by_tag_name('body').text)

        self.is_logged_in = True

    def test_can_logout_user(self):
        if not self.is_logged_in:
            self.login_test_user()
            self.is_logged_in = True

        # now log them out
        self.load_selenium_page(view_name='pswebsite:logout')

        # to test, the user's name should not appear at the index page
        # after the redirect
        self.assertNotIn(test_user_data['username'],
                         self.selenium.find_element_by_tag_name('body').text)
        self.is_logged_in = False
