from selenium import webdriver
import unittest


class MiScriptSelenium(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''Run once when class is loaded'''
        # SET CONFIGURATION
        cls.url = 'http://localhost:8080/kanboard-1.2.3'
        cls.user_name = 'admin'
        cls.user_pwd = 'admin'

    def setUp(self):
        '''Run once before each test case'''
        # Open the browser driver
        self.browser = webdriver.Chrome('/tmp/seleniumWebDrivers/chromedriver')

    # TIPS:
    # Create method actions: Extract these methods into a Library module.
    # Create a map file: Correlate screen elements and it text-ids - When
    # element needs to be updated, it is done in one central location.

    # I'll leave it here for now:

    def _signin_to_kanboard(self, url, user_name, user_pwd):
        '''Method to sign into kanboard web application'''

        # Direct browser to given URL
        self.browser.get(url)

        # Find username element and type given value
        user_in = self.browser.find_element_by_id('form-username')
        user_in.send_keys(user_name)

        # Find userpassword element and type given value
        pwd_in = self.browser.find_element_by_id('form-password')
        pwd_in.send_keys(user_pwd)

        # Click sign in button
        signin_btn = self.browser.\
            find_element_by_css_selector('button.btn.btn-blue')
        signin_btn.click()

    def test_kanboard_signin_good_credentials(self):
        self._signin_to_kanboard(self.url, self.user_name, self.user_pwd)
        # Verify we actually login
        header = self.browser.find_element_by_css_selector('h1')
        htext = header.text if hasattr(header, 'text') else ''
        self.assertEqual(htext, 'KB Dashboard for admin')

    def tearDown(self):
        '''Run once after each test case'''
        # Close the browser - cleanup
        self.browser.close()

if __name__ == '__main__':
    unittest.main()