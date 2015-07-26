from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase

from django.core.urlresolvers import reverse

from pswebsite.tests.test_settings import test_data
from pswebsite.utils import url_with_querystring

from selenium.webdriver.firefox.webdriver import WebDriver

class ViewTest(TestCase):
    fixtures = [test_data]

    def get_res(self, view_name=None, args=None, kwargs=None,
                **querystring_args):
        if not view_name:
            view_name = self.view_name

        url = reverse(view_name, args=args, kwargs=kwargs)
        return self.client.get(url_with_querystring(url, **querystring_args))

# For some reason, this isn't allowed to inherit from ViewTest, or fails
class SeleniumTest(StaticLiveServerTestCase):
    """ A selenium test. Uses the firefox web driver.
        This is a subclass of both StaticLiveServerTestCase and ViewTest
    """
    fixtures = [test_data]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    # def setUp(self):
    #     self.load_selenium_page()

    def load_selenium_page(self, view_name, args=None, kwargs=None):
        url = "{}{}".format(self.live_server_url,
                            reverse(view_name, args=args, kwargs=kwargs))
        self.selenium.get(url)
