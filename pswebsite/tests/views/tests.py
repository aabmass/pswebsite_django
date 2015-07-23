from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from pswebsite.tests.test_types import SeleniumTest, ViewTest
from pswebsite.tests.test_settings import test_user_data

# TODO: add tests for Register already registered user
# and trying to login non-registered username. These
# have to be Selenium since they will test the parsley
# frontend AJAX form validation

class IndexViewTests(ViewTest):
    view_name = 'pswebsite:index'

    def test_shows_login_menu(self):
        res = self.get_res()
        self.assertContains(res, "Login")

    def test_shows_register_menu(self):
        res = self.get_res()
        self.assertContains(res, "Register")

class UserExistsViewTests(ViewTest):
    view_name = 'pswebsite:userexists'

    def test_returns_2xx_for_existing_user(self):
        res = self.get_res(username=test_user_data['username'])

        self.assertGreaterEqual(res.status_code, 200)
        self.assertLessEqual(res.status_code, 299)

    #def test_returns_404_for_non_existant_user(self):

class RegisterViewTests(SeleniumTest):
    def test_register_form_can_register_new_user(self):
        new_username = "register@test.com"

        self.load_selenium_page('pswebsite:register')
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys(new_username)
        first_name_input = self.selenium.find_element_by_name("first_name")
        first_name_input.send_keys("Regist")
        last_name_input = self.selenium.find_element_by_name("last_name")
        last_name_input.send_keys("Err")
        password1_input = self.selenium.find_element_by_name("password1")
        password1_input.send_keys("register")
        password2_input = self.selenium.find_element_by_name("password2")
        password2_input.send_keys("register")

        self.selenium.find_element_by_xpath('//input[@value="Create User"]').click()

        # test that user got logged in
        self.assertIn(new_username,
                      self.selenium.find_element_by_tag_name('body').text)

        # now make sure the user is in the database too
        user = User.objects.get(username=new_username)
        self.assertIsNotNone(user)

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
