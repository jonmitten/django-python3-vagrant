'''
these tests should be run from
the host computer

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference("browser.cache.disk.enable", False)
        self.profile.set_preference("browser.cache.memory.enable", False)
        self.profile.set_preference("browser.cache.offline.enable", False)
        self.profile.set_preference("network.http.use-cache", False)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    def check_for_row_in_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She
        # goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # She types "Buy Peacock Feathers" into a text box (Edith's
        # hobby is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and the new page lists
        # " 1 : Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)

        # element = self.browser.find_element_by_tag_name('table')
        # source_code = element.get_attribute("outerHTML")
        # print("\n\n{}\n\n".format(source_code))


        # There is still a text box inviting her to add another item
        # She enteres "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_table('1: Buy peacock feathers')
        self.check_for_row_in_table('2: Use peacock feathers to make a fly')

        # Edith wonders whether the site will ermember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect
        self.fail('Finish the test!')

        # She visits the URL - her to-do list is still there


if __name__ == '__main__':
    unittest.main(warnings='ignore')
