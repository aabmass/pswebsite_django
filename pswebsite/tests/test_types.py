from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase

from django.core.urlresolvers import reverse

from selenium.webdriver.firefox.webdriver import WebDriver

class ViewTest(TestCase):
    def get_res(self, view_name=None, args=None, kwargs=None):
        if not view_name:
            view_name = self.view_name
        return self.client.get(reverse(self.view_name, args, kwargs))

class SeleniumTest(StaticLiveServerTestCase, ViewTest):
    """ A selenium test. Uses the firefox web driver.
        This is a subclass of both LiveServerTestCase and ViewTest
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def load_selenium_page(self, view_name=None, args=None, kwargs=None):
        if not view_name:
            view_name = self.view_name
        url = "{}{}".format(self.live_server_url,
                            reverse(self.view_name, args, kwargs))
        self.selenium.get(url)

    def setUp(self):
        self.load_selenium_page()
