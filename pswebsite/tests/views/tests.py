from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from pswebsite.tests.test_types import SeleniumTest, ViewTest
from pswebsite.tests.test_settings import test_data, test_user_data

from pswebsite.forms import RegisterForm

user = None

def create_new_user(email="tester@gmail.com",
                    first_name="Test",
                    last_name="Er",
                    password="tester"):
    """ Create a new user and return a tuple of the user
        object and the user_data, so that we know the password
        and any other hashed fields original values
    """

    # can probably be done more elegantly with args/kwargs
    user_data = {
        'email': email,
        'username': email,
        'first_name': first_name,
        'last_name': last_name,
        'password': password,
    }

    user = User.objects.create_user(email, email=email, password=password,
                                    first_name=first_name, last_name=last_name)
    user.save()
    return (user, user_data)


#def login_user_completely(user):

#def logout_user_completely(user):

class IndexViewTests(ViewTest):
    view_name = 'pswebsite:index'

    def test_shows_login_menu(self):
        res = self.get_res()
        self.assertContains(res, "Login")

    def test_shows_register_menu(self):
        res = self.get_res()
        self.assertContains(res, "Register")

    #def test_doesnt_show_register_menu_if_logged_in(self):

    #def test_doesnt_show_login_menu_if_logged_in(self):

    #def test_shows_user_menu_if_logged_in(self):

# This appears impossible for some reason. IDK what the problem is
# appears that the user I create isn't getting saved to the test DB
# and when the selenium post finally gets to the view, the user is
# no longer in the database.... Shame on django, this is pathetic.
# I want to test logging in and it appears impossible. Documentation
# is, of course, completely useless, not fulling documenting the API
# or which methods can/should be overriden as hooks in which classes
# or what these methods do. For some reason, django thinks that the best
# course of action is to make the developer search their tutorial and
# documentation that describes "common" uses (as deemed by them).
# Apparently, documenting testing logging in is too not common enough
# for them.
#
# Even more dissappointing, I see answers appearing everywhere not running
# into this problems. This is really bothering me and I'm quite irritated
# and frankly feeling defeated by my attempts to create a fucking test.
#
# Note: there appears a very vague and underqualified statement in the official
# "documentation" on this subject. Appearing in a comment in a brief code
# example, the documentation vaguely states that:
# # Recall that middleware are not supported. You can simulate a
# # logged-in user by setting request.user manually.
# .... well that is useless for doing a selenium test and actually
# seeing if your app is broken or not


class LoginLogoutViewTests(SeleniumTest):
    fixtures = [test_data]

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



### TESTS
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class MySeleniumTests(LiveServerTestCase):
    fixtures = ['testdata.json']

    @classmethod
    def setUpClass(cls):
        super(MySeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('tester@test.com')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('tester123')
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
